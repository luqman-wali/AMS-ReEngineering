# Architecture Views Documentation - AMS

## Table of Contents
1. [Logical View](#logical-view)
2. [Physical View](#physical-view)
3. [Process View](#process-view)
4. [Implementation View](#implementation-view)
5. [Current State Analysis](#current-state-analysis)

---

## Logical View

### Purpose
Represents the functional decomposition of the system into logical components and subsystems.

### Components

#### 1. **Airline Management Component**
- **Responsibility**: Manage airlines, their details, and aircraft
- **Interfaces**:
  - `addAirline(name, iata_code, country)` → returns airline_id
  - `updateAirline(airline_id, details)` → returns status
  - `getAirline(airline_id)` → returns airline object
- **Dependencies**: Database, Validation Service
- **Relationships**: 
  - Owns Aircraft Component
  - Employs Crew Component

#### 2. **Flight Management Component**
- **Responsibility**: Create and manage flight routes and schedules
- **Interfaces**:
  - `createRoute(source, destination, date, schedule)` → returns route_id
  - `updateFlightStatus(route_id, status)` → returns status
  - `getFlightInfo(route_id)` → returns flight details
- **Dependencies**: Airline, Airport, Aircraft components
- **Relationships**: 
  - References Airport Component
  - Uses Aircraft Component
  - Assigns Crew Component

#### 3. **Passenger Management Component**
- **Responsibility**: Register and manage passenger information
- **Interfaces**:
  - `registerPassenger(details)` → returns passenger_id
  - `updatePassenger(passenger_id, details)` → returns status
  - `getPassenger(passenger_id)` → returns passenger object
- **Dependencies**: Database, Validation Service
- **Relationships**:
  - Creates bookings in Booking Component
  - Has emergency contacts

#### 4. **Airport Operations Component**
- **Responsibility**: Manage airports, runways, terminals, and staff
- **Interfaces**:
  - `addAirport(name, iata_code, location)` → returns airport_id
  - `manageRunway(airport_id, runway_details)` → returns runway_id
  - `manageTerminal(airport_id, terminal_details)` → returns terminal_id
- **Dependencies**: Database, Validation Service
- **Relationships**:
  - Employs Airport Staff
  - Serves Flight Component

#### 5. **Booking Management Component**
- **Responsibility**: Create and manage passenger bookings
- **Interfaces**:
  - `createBooking(passenger_id, route_id, date)` → returns booking_id
  - `generateBoardingPass(booking_id)` → returns boarding pass
  - `cancelBooking(booking_id)` → returns refund info
- **Dependencies**: Passenger, Flight, Payment Service
- **Relationships**:
  - References Flight Component
  - References Passenger Component
  - Manages Special Services
  - Tracks Luggage

#### 6. **Crew Management Component**
- **Responsibility**: Manage airline and airport personnel
- **Interfaces**:
  - `registerCrew(type, details)` → returns crew_id
  - `assignCrewToFlight(crew_id, route_id)` → returns assignment_id
  - `getCrewInfo(crew_id)` → returns crew details
- **Dependencies**: Database, Validation Service
- **Relationships**:
  - Owned by Airline Component
  - Employed by Airport Operations Component
  - Assigned to Flight Component

### Logical Architecture Diagram

```
┌─────────────────────────────────────────────────────┐
│              User Interface (CLI)                    │
└─────────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────────┐
│         Business Logic Layer                         │
├──────────┬──────────┬──────────┬──────────┬─────────┤
│ Airline  │ Flight   │Passenger │ Airport  │ Booking │
│Management│Management│Management│Operations│Management
│Component │Component │Component │Component │Component
├──────────┴──────────┴──────────┴──────────┴─────────┤
│         Crew Management Component                    │
└─────────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────────┐
│      Validation & Data Access Services              │
│  • Input Validation Service                          │
│  • Database Access Service                           │
│  • Payment Service                                   │
└─────────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────────┐
│         MySQL Database (airport_db)                  │
│  • 30+ Tables                                        │
│  • Complex Relationships                             │
│  • Foreign Key Constraints                           │
└─────────────────────────────────────────────────────┘
```

---

## Physical View

### Purpose
Represents the system's physical deployment, hardware, and runtime environment.

### Deployment Components

#### Client Machine
- **OS**: Windows/Linux/Mac
- **Python**: 3.6+
- **Dependencies**:
  - PyMySQL library
  - Tabulate library
  - System libraries

#### Application Server
- **Runtime**: Python interpreter
- **Modules**:
  - add.py - Create operations
  - read.py - Read operations
  - update.py - Modify operations
  - delete.py - Delete operations
  - extra.py - Additional features
  - miniworld.py - Test data

#### Network
- **Protocol**: TCP/IP
- **Port**: 3306 (MySQL standard)
- **Connection Type**: Direct or tunneled

#### Database Server
- **DBMS**: MySQL Server (5.7+)
- **Storage Engine**: InnoDB
- **Database**: airport_db
- **Tables**: 30+ normalized tables

#### Storage
- **Type**: Hard Drive / SSD
- **Capacity**: As needed for data
- **Backup**: Manual or scheduled

### Physical Deployment Diagram

```
┌──────────────────────┐
│  Client Tier         │
│  ┌────────────────┐  │
│  │ Python CLI App │  │
│  │ (User Input)   │  │
│  └────────────────┘  │
└──────────────────────┘
         ↓
┌──────────────────────────────────┐
│  Application Tier                │
│  ┌──────────────────────────────┐│
│  │ Python Modules               ││
│  │ • add.py, read.py, etc       ││
│  │ • PyMySQL Driver             ││
│  │ • Business Logic             ││
│  └──────────────────────────────┘│
└──────────────────────────────────┘
         ↓
    [TCP/IP:3306]
         ↓
┌──────────────────────────────────┐
│  Database Tier                   │
│  ┌──────────────────────────────┐│
│  │ MySQL Server                 ││
│  │ • airport_db Database        ││
│  │ • InnoDB Storage Engine      ││
│  │ • 30+ Tables                 ││
│  └──────────────────────────────┘│
└──────────────────────────────────┘
         ↓
    [Physical Storage]
         ↓
┌──────────────────────┐
│ Storage Tier         │
│ • Hard Drive / SSD   │
│ • Data Files         │
│ • Backups            │
└──────────────────────┘
```

---

## Process View

### Purpose
Represents the dynamic aspects and process flows of the system.

### Key Processes

#### 1. **Flight Booking Process**
**Sequence**:
1. User searches for flights
2. System queries available routes
3. User selects flight and date
4. User enters passenger details
5. System validates data
6. User selects seat and services
7. System processes payment
8. System generates boarding pass
9. System sends confirmation

**Actors**: Passenger, System
**Outcome**: Booking confirmed, PNR issued
**Duration**: ~5-10 minutes
**Error Handling**: Validation failures, payment failures

#### 2. **Flight Scheduling Process**
**Sequence**:
1. Airline staff creates route
2. System validates route
3. Airline assigns aircraft
4. Airline assigns crew
5. System adds stopovers
6. System publishes flight

**Actors**: Airline Staff, System
**Outcome**: Flight scheduled and published
**Duration**: ~20-30 minutes
**Error Handling**: Conflicts, resource unavailability

#### 3. **Passenger Check-in Process**
**Sequence**:
1. Passenger presents boarding pass
2. System verifies boarding pass
3. System checks luggage
4. System assigns baggage tags
5. System confirms seat
6. System prints gate info

**Actors**: Airport Staff, Passenger, System
**Outcome**: Passenger checked in
**Duration**: ~5-10 minutes
**Error Handling**: Invalid pass, missed deadline

---

## Implementation View

### Purpose
Shows the organization of source code and modules.

### Source Code Organization

```
Central-Airport-Management-System/
├── add.py                    (1450 LOC - CRUD Create)
├── read.py                   (40 LOC - CRUD Read)
├── update.py                 (500 LOC - CRUD Update)
├── delete.py                 (300 LOC - CRUD Delete)
├── extra.py                  (350 LOC - Extra Features)
├── miniworld.py              (400 LOC - Test Data)
├── phase0.sql                (Database Schema)
├── phase1-5.sql              (Additional Schemas)
└── README.md                 (Documentation)
```

### Module Responsibilities

| Module | Responsibility | Size | Complexity |
|--------|-----------------|------|-------------|
| add.py | Airline, Aircraft, Route, Passenger, Booking creation | 1450 LOC | HIGH |
| read.py | Query and display data | 40 LOC | LOW |
| update.py | Update airline, flight, crew records | 500 LOC | MEDIUM |
| delete.py | Delete bookings, passengers | 300 LOC | MEDIUM |
| extra.py | Additional operations | 350 LOC | MEDIUM |
| miniworld.py | Generate test data | 400 LOC | MEDIUM |

---

## Current State Analysis

### Strengths

1. **Comprehensive Schema**
   - Well-designed database with proper relationships
   - Appropriate use of foreign keys
   - Good normalization

2. **Feature Complete**
   - Covers all major airport operations
   - Flexible data model
   - Multiple user types supported

3. **Direct Database Access**
   - Simple implementation
   - Direct control over queries
   - No abstraction overhead

### Weaknesses

1. **Monolithic Application**
   - All logic in one layer
   - No separation of concerns
   - Difficult to test
   - Hard to scale

2. **God Methods**
   - add.py contains 50+ functions
   - Each function does multiple things
   - High cyclomatic complexity
   - Difficult to maintain

3. **Tight Coupling**
   - Direct dependencies on PyMySQL
   - Business logic mixed with data access
   - Hard to change implementation
   - Difficult to test without database

4. **Code Duplication**
   - Similar validation patterns repeated
   - Duplicate error handling
   - Repeated connection logic

5. **Poor Error Handling**
   - Basic try-catch blocks
   - Limited error information
   - No logging mechanism
   - No rollback strategy

### Opportunities for Improvement

1. **Introduce Service Layer**
   - Separate business logic from data access
   - Improve testability
   - Enable code reuse

2. **Implement Repository Pattern**
   - Abstract database access
   - Enable different storage implementations
   - Simplify testing

3. **Add API Layer**
   - REST API for external integration
   - Multiple client support
   - Better scalability

4. **Improve Error Handling**
   - Comprehensive logging
   - Better error messages
   - Transaction management

5. **Add Testing Framework**
   - Unit tests
   - Integration tests
   - Mock data generators

---

**Document Version**: 1.0
**Last Updated**: June 2026
**Status**: Active
