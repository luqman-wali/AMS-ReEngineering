# Project Code - Central Airport Management System

## Source Code Analysis

This folder contains the original legacy code from the Central Airport Management System (AMS) repository.

### Folder Structure
```
project_code/
├── original/           # Original untouched legacy code
│   ├── add.py
│   ├── read.py
│   ├── update.py
│   ├── delete.py
│   ├── extra.py
│   ├── miniworld.py
│   └── phase0.sql
│       phase1.sql
│       phase2.sql
│       phase3.sql
│       phase4.sql
│       phase5.sql
└── analyzed/           # Code with analysis annotations (coming soon)
```

## Key Observations from Legacy Code

### Python Code (CRUD Operations)
1. **add.py** (46 KB)
   - Multiple monolithic functions
   - Tight coupling between UI and DB logic
   - No proper error handling
   - Code duplication

2. **read.py** (855 B)
   - Simple query execution
   - Basic tabulation of results

3. **update.py, delete.py, extra.py**
   - Similar pattern to add.py
   - Multiple responsibilities per function

### Database Schema (SQL)
1. **phase0-5.sql**
   - Complex table relationships
   - Poor naming conventions (spaces in column names)
   - Circular dependencies
   - Inconsistent data types

## Code Smells Identified

### High Priority
- [ ] God classes/methods with multiple responsibilities
- [ ] Tight coupling between layers
- [ ] Monolithic functions
- [ ] Poor naming conventions
- [ ] No separation of concerns

### Medium Priority
- [ ] Code duplication
- [ ] Inconsistent error handling
- [ ] Magic numbers and strings
- [ ] Missing documentation

### Low Priority
- [ ] Formatting inconsistencies
- [ ] Long parameter lists

## Next Steps

1. Perform detailed cyclomatic complexity analysis
2. Generate code metrics reports
3. Create refactored versions
4. Document architectural improvements
5. Design modernization strategy
