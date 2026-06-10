# Process & Data Flow Diagram - AMS

## Flight Booking Process Flow

```mermaid
graph TD
    START(["Passenger Initiates Booking"]) --> SEARCH["Search Available Flights"]
    SEARCH --> VERIFY{"Flight<br/>Available?"}
    VERIFY -->|No| NOSEARCH["Show No Results"]
    NOSEARCH --> END1(["Process Ends"])
    
    VERIFY -->|Yes| SELECT["Select Flight & Route"]
    SELECT --> PDETAILS["Enter Passenger Details"]
    PDETAILS --> VALIDATE{"Validate<br/>Details?"}
    VALIDATE -->|Invalid| ERROR1["Show Error Message"]
    ERROR1 --> PDETAILS
    
    VALIDATE -->|Valid| SEAT["Select Seat"]
    SEAT --> BAGGAGE["Add Luggage"]
    BAGGAGE --> SERVICES["Select Special Services"]
    SERVICES --> PAYMENT["Process Payment"]
    PAYMENT --> CONFIRM{"Payment<br/>Successful?"}
    
    CONFIRM -->|Failed| RETRY["Retry Payment"]
    RETRY --> PAYMENT
    CONFIRM -->|Success| GENERATE["Generate Boarding Pass"]
    GENERATE --> SAVE["Save to Database"]
    SAVE --> SUCCESS(["Booking Confirmed"])
```

## Data Flow Diagram - Flight Management

```mermaid
graph LR
    USER["User/Admin"] -->|Input| ADDPY["add.py<br/>(CRUD Module)"]
    ADDPY -->|Validate| VAL["Validation<br/>Functions"]
    VAL -->|Check| DB[("Database<br/>airport_db")]
    DB -->|Return Status| ADDPY
    ADDPY -->|Insert/Update| DB
    ADDPY -->|Output| USER
    
    DB -->|Read| READPY["read.py<br/>(Query Module)"]
    READPY -->|Display| USER
    READPY -->|Format| TABULATE["Tabulate<br/>Library"]
    TABULATE -->|Display| USER
```

## System Data Flow (High Level)

```mermaid
graph TB
    subgraph "User Operations"
        ADD["Create<br/>(Airline, Flight, Passenger)"]
        READ["Read<br/>(View Records)"]
        UPDATE["Update<br/>(Modify Records)"]
        DELETE["Delete<br/>(Remove Records)"]
    end
    
    subgraph "Processing"
        VAL["Validation<br/>Service"]
        TRANS["Transaction<br/>Management"]
        ERROR["Error<br/>Handling"]
    end
    
    subgraph "Database Layer"
        AIRLINE["Airline<br/>Table"]
        FLIGHT["Flight<br/>Table"]
        PASSENGER["Passenger<br/>Table"]
        BOOKING["Booking<br/>Table"]
        CREW["Crew<br/>Table"]
        AIRPORT["Airport<br/>Table"]
    end
    
    ADD -->|validate| VAL
    READ -->|validate| VAL
    UPDATE -->|validate| VAL
    DELETE -->|validate| VAL
    
    VAL -->|manage| TRANS
    TRANS -->|handle| ERROR
    
    ADD -->|insert| AIRLINE
    ADD -->|insert| FLIGHT
    ADD -->|insert| PASSENGER
    ADD -->|insert| BOOKING
    ADD -->|insert| CREW
    ADD -->|insert| AIRPORT
    
    READ -->|query| AIRLINE
    READ -->|query| FLIGHT
    READ -->|query| PASSENGER
    READ -->|query| BOOKING
    
    UPDATE -->|modify| AIRLINE
    UPDATE -->|modify| FLIGHT
    UPDATE -->|modify| PASSENGER
    
    DELETE -->|remove| BOOKING
    DELETE -->|remove| PASSENGER
```

## Database Transaction Flow

```
User Input
    ↓
Validation (date, format, constraints)
    ↓
Transaction Begin
    ↓
Execute Query (INSERT/UPDATE/DELETE)
    ↓
Check Constraints & Foreign Keys
    ↓
Success? ──Yes→ COMMIT → Persist to Storage
    │
    └─No→ ROLLBACK → Undo Changes → Error Message to User
```

## Data Dependencies

```
Airline
    ↓
Aircraft (owns aircraft)
Airline_Crew (employs crew)
    ↓
Route (has flights)
Flight (operated by aircraft & crew)
    ↓
Passenger (books flight)
Boarding Pass (issued for flight)
    ↓
Luggage (associated with boarding pass)
```

## Key Observations

### Current Flow Issues
1. **No middleware** - Direct DB access
2. **Synchronous operations** - Blocking calls
3. **No logging** - No audit trail
4. **No caching** - Every operation hits DB
5. **Limited error handling** - Basic try-catch only

### Recommended Improvements
1. **Add logging layer** - Track all operations
2. **Implement queue system** - Async processing
3. **Add caching** - Redis for frequently accessed data
4. **Event-driven architecture** - For complex workflows
5. **API layer** - For external integrations
