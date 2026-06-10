# Sequence Diagram - AMS Flight Booking Process

## Flight Booking Sequence

```mermaid
sequenceDiagram
    participant P as Passenger
    participant UI as System UI
    participant APP as Application Logic
    participant VAL as Validation Service
    participant DB as Database
    participant PAY as Payment Gateway
    participant EMAIL as Email Service
    
    P->>UI: 1. Search Flights
    activate UI
    UI->>APP: 2. searchFlights(date, airports)
    activate APP
    APP->>DB: 3. Query Routes
    activate DB
    DB-->>APP: 4. Return Available Routes
    deactivate DB
    APP-->>UI: 5. Return Flight List
    deactivate APP
    UI-->>P: 6. Display Flights
    deactivate UI
    
    P->>UI: 7. Select Flight & Enter Details
    activate UI
    UI->>APP: 8. createBooking(flightId, passengerDetails)
    activate APP
    
    APP->>VAL: 9. Validate Passenger Details
    activate VAL
    VAL->>DB: 10. Check Aadhar Exists
    activate DB
    DB-->>VAL: 11. Aadhar Valid/Invalid
    deactivate DB
    VAL-->>APP: 12. Validation Result
    deactivate VAL
    
    alt Validation Failed
        APP-->>UI: 13. Show Error
        UI-->>P: 14. Display Error Message
    else Validation Passed
        APP->>DB: 15. Lock Flight Seat
        activate DB
        DB-->>APP: 16. Seat Reserved
        deactivate DB
        
        P->>UI: 17. Confirm & Make Payment
        UI->>PAY: 18. Process Payment(amount)
        activate PAY
        PAY-->>UI: 19. Payment Status
        deactivate PAY
        
        alt Payment Successful
            UI->>APP: 20. Confirm Booking
            activate APP
            APP->>DB: 21. Create Booking Record
            activate DB
            DB->>DB: 22. Insert into boarding_pass
            DB->>DB: 23. Insert into luggage
            DB->>DB: 24. Insert into special_services
            DB-->>APP: 25. Booking ID
            deactivate DB
            
            APP->>EMAIL: 26. Send Confirmation
            activate EMAIL
            EMAIL-->>APP: 27. Email Sent
            deactivate EMAIL
            
            APP-->>UI: 28. Booking Confirmed
            deactivate APP
            UI-->>P: 29. Display Boarding Pass
        else Payment Failed
            UI->>APP: 30. Release Seat Lock
            activate APP
            APP->>DB: 31. Unlock Seat
            activate DB
            DB-->>APP: 32. Seat Released
            deactivate DB
            deactivate APP
            UI-->>P: 33. Payment Failed - Retry
        end
    end
```

## Flight Cancellation Sequence

```mermaid
sequenceDiagram
    participant P as Passenger
    participant UI as System UI
    participant APP as Application
    participant DB as Database
    participant REFUND as Refund Service
    participant EMAIL as Email Service
    
    P->>UI: 1. Request Cancellation
    activate UI
    UI->>APP: 2. cancelBooking(bookingId)
    activate APP
    
    APP->>DB: 3. Check Flight Status
    activate DB
    DB-->>APP: 4. Flight Status
    deactivate DB
    
    alt Flight Already Departed
        APP-->>UI: 5. Cannot Cancel
        UI-->>P: 6. Show Error
    else Flight Not Departed
        APP->>REFUND: 7. Calculate Refund Amount
        activate REFUND
        REFUND-->>APP: 8. Refund Amount
        deactivate REFUND
        
        APP->>DB: 9. Cancel Booking
        activate DB
        DB->>DB: 10. Update booking_pass status
        DB->>DB: 11. Release seat
        DB->>DB: 12. Release luggage
        DB-->>APP: 13. Cancellation Confirmed
        deactivate DB
        
        APP->>REFUND: 14. Process Refund
        activate REFUND
        REFUND-->>APP: 15. Refund Processed
        deactivate REFUND
        
        APP->>EMAIL: 16. Send Cancellation Email
        activate EMAIL
        EMAIL-->>APP: 17. Email Sent
        deactivate EMAIL
        
        APP-->>UI: 18. Cancellation Complete
        deactivate APP
        UI-->>P: 19. Show Confirmation
    end
```

## Database Transaction Sequence

```mermaid
sequenceDiagram
    participant APP as Application
    participant TRANS as Transaction Manager
    participant DB as MySQL Database
    participant STORAGE as Physical Storage
    
    APP->>TRANS: 1. BEGIN TRANSACTION
    activate TRANS
    
    TRANS->>DB: 2. Start Transaction
    activate DB
    
    APP->>DB: 3. INSERT Booking Record
    DB->>DB: 4. Validate Constraints
    DB->>DB: 5. Acquire Row Locks
    DB-->>APP: 6. Insert Successful
    
    APP->>DB: 7. INSERT Luggage Record
    DB->>DB: 8. Check Foreign Keys
    DB-->>APP: 9. Insert Successful
    
    APP->>DB: 10. UPDATE Aircraft Status
    DB-->>APP: 11. Update Successful
    
    alt All Operations Successful
        APP->>TRANS: 12. COMMIT
        TRANS->>DB: 13. Commit Transaction
        DB->>STORAGE: 14. Persist to Disk
        STORAGE-->>DB: 15. Data Saved
        DB->>DB: 16. Release Locks
        DB-->>TRANS: 17. Commit Confirmed
        TRANS-->>APP: 18. Transaction Complete
        deactivate TRANS
        deactivate DB
    else Operation Failed
        APP->>TRANS: 19. ROLLBACK
        TRANS->>DB: 20. Rollback Transaction
        DB->>DB: 21. Undo All Changes
        DB->>DB: 22. Release Locks
        DB-->>TRANS: 23. Rollback Confirmed
        TRANS-->>APP: 24. Transaction Rolled Back
        deactivate TRANS
        deactivate DB
    end
```

## Error Handling Sequence

```mermaid
sequenceDiagram
    participant USER as User
    participant APP as Application
    participant DB as Database
    participant LOG as Logger
    participant ALERT as Alert Service
    
    USER->>APP: 1. Request Operation
    activate APP
    
    APP->>DB: 2. Execute Query
    activate DB
    
    alt Success
        DB-->>APP: 3. Return Data
        APP-->>USER: 4. Display Result
    else Error Occurs
        DB-->>APP: 3. Error: Connection Lost
        deactivate DB
        
        APP->>LOG: 4. Log Error
        activate LOG
        LOG-->>APP: 5. Logged
        deactivate LOG
        
        APP->>ALERT: 6. Send Alert
        activate ALERT
        ALERT-->>APP: 7. Alert Sent
        deactivate ALERT
        
        APP-->>USER: 8. Show Error Message
        activate USER
        USER->>APP: 9. Retry Request
        deactivate USER
        deactivate APP
    end
```

## Performance Considerations

### Current Flow Issues
1. **No caching** - Every search queries entire table
2. **No connection pooling** - New connection per request
3. **No pagination** - Returns all results
4. **No async operations** - Blocking calls
5. **No load balancing** - Single database

### Optimization Opportunities
1. **Add Redis cache** - Cache flight searches
2. **Connection pooling** - Reuse connections
3. **Pagination** - Limit result sets
4. **Async operations** - Non-blocking calls
5. **Database indexing** - Faster queries
6. **Read replicas** - Distribute read load
