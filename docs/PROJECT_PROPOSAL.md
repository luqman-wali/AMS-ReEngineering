# AMS Re-Engineering Project Proposal

## Executive Summary

This document outlines the architecture recovery and model-driven re-engineering of the Central Airport Management System (AMS). The AMS is a legacy DBMS application built in Python and MySQL that manages critical airport operations including flights, passengers, bookings, and staff management.

### Project Justification
The system has accumulated significant technical debt through years of development:
- **Monolithic architecture** with tight coupling between modules
- **God classes/methods** handling multiple responsibilities
- **Poor code organization** with duplicated logic
- **Inadequate testing** and documentation
- **Scalability concerns** limiting growth

This re-engineering project aims to modernize the system while maintaining business functionality.

---

## System Selection: Central Airport Management System

### System Overview
- **Name**: Central Airport Management System (AMS)
- **Domain**: Airport Operations Management
- **Technology Stack**: Python + MySQL
- **Size**: ~46 KB Python code + Complex SQL schema
- **Source**: https://github.com/Samyak005/Central-Airport-Management-System-Database

### Key Features
1. **Airline Management**
   - Add/update airlines
   - Track aircraft inventory
   - Manage airline details and status

2. **Flight Management**
   - Create and schedule routes
   - Manage flight status
   - Track stopovers

3. **Passenger Management**
   - Register passengers
   - Manage passenger records
   - Emergency contact tracking

4. **Airport Operations**
   - Manage runways and terminals
   - Track capacity and resources
   - Coordinate airport staff

5. **Booking System**
   - Create reservations
   - Generate boarding passes
   - Manage special services
   - Track luggage

6. **Crew Management**
   - Manage airline crew (pilots, attendants, engineers)
   - Track airport staff (ATC, security, management)
   - Language proficiency tracking

---

## Project Scope

### Phase 1: Program Comprehension & Documentation Analysis
**Duration**: 2 weeks
**Deliverables**:
- Source code review and analysis
- System architecture documentation
- Functionality mapping
- External dependencies identification

### Phase 2: Reverse Engineering & Architecture Recovery
**Duration**: 3 weeks
**Deliverables**:
- Recovered logical architecture (3 views)
- Component and module relationships
- Design patterns identification
- Database schema analysis

### Phase 3: Static & Dynamic Code Analysis
**Duration**: 3 weeks
**Deliverables**:
- Code complexity metrics (Cyclomatic Complexity)
- Coupling and cohesion analysis
- Code smell detection
- Duplicate code identification
- Test coverage report

### Phase 4: Code Restructuring & Refactoring
**Duration**: 4 weeks
**Deliverables**:
- Refactored code samples (5-10 modules)
- Design pattern applications
- Improved code quality metrics
- Refactoring documentation with justifications

### Phase 5: Modernization Strategy Formulation
**Duration**: 2 weeks
**Deliverables**:
- Current state analysis
- Modernization approaches (OO/Component-based, SOA/Microservices, Cloud)
- Migration roadmap (5-phase plan)
- Cost-benefit analysis
- Risk assessment

---

## Expected Outcomes

### Deliverables
1. ✅ **Comprehensive Source Code Metrics Report**
   - LOC (Lines of Code)
   - Complexity metrics
   - Coupling & cohesion analysis
   - Code smell summary

2. ✅ **Recovered Architecture Diagrams** (3 Views)
   - Logical view (components & responsibilities)
   - Physical view (deployment & infrastructure)
   - Process view (data flow & sequences)

3. ✅ **Identified Code Smells & Anti-patterns**
   - God classes/methods
   - Tight coupling
   - Code duplication
   - Poor naming conventions
   - Missing error handling

4. ✅ **Refactored Code Samples**
   - 5-10 modules with improvements
   - Design pattern applications
   - Documentation and justification
   - Before/after comparison

5. ✅ **Modernization Strategy Document**
   - Current state analysis
   - Multiple modernization approaches
   - Detailed migration roadmap
   - Implementation timeline
   - Resource requirements

6. ✅ **Final Technical Report**
   - Executive summary
   - Detailed findings
   - Recommendations
   - Conclusion

---

## Tools & Technologies

### Static Analysis
- **Pylint** - Code quality and complexity
- **CodeClimate** - Maintainability index
- **SonarQube** - Comprehensive analysis
- **Radon** - Python metrics

### Modeling & Documentation
- **Draw.io** - Architecture diagrams
- **StarUML** - UML modeling
- **Visual Paradigm** - System design
- **Mermaid** - Diagram generation

### Version Control & Collaboration
- **GitHub** - Repository hosting
- **Git** - Version control
- **GitHub Issues** - Task tracking
- **GitHub Projects** - Planning

### Testing & Quality
- **Pytest** - Unit testing
- **Coverage.py** - Code coverage
- **SonarQube** - Quality gates

### Documentation
- **Markdown** - Documentation format
- **Sphinx** - API documentation
- **Doxygen** - Code documentation

---

## Team Structure

### Team Members
| Role | Name | Responsibility |
|------|------|----------------|
| **Project Lead** | luqman-wali | Overall coordination, architecture decisions |
| **Senior Analyst** | TBD | Code analysis, metrics reporting |
| **Architect** | TBD | Architecture recovery, design |
| **Developer** | TBD | Refactoring, code improvements |
| **QA Engineer** | TBD | Testing, validation |

### Skills Required
- Python programming (Advanced)
- Database design (MySQL/SQL)
- Software architecture
- Code quality analysis
- Documentation and communication

---

## Project Timeline

```
Week 1-2:   Phase 1 - Program Comprehension
            ├─ Source code review
            ├─ System documentation
            └─ Requirements mapping

Week 3-5:   Phase 2 - Reverse Engineering
            ├─ Architecture recovery
            ├─ Component identification
            └─ Design pattern analysis

Week 6-8:   Phase 3 - Code Analysis
            ├─ Metrics collection
            ├─ Code smell detection
            └─ Report generation

Week 9-12:  Phase 4 - Refactoring
            ├─ Code improvements
            ├─ Pattern application
            └─ Testing & validation

Week 13-14: Phase 5 - Modernization
            ├─ Strategy formulation
            ├─ Roadmap creation
            └─ Final report
```

---

## Success Criteria

### Metrics
- ✓ Code complexity reduced by 30%+
- ✓ Cyclomatic complexity < 10 per function
- ✓ Code duplication reduced by 25%+
- ✓ Test coverage improved by 40%+
- ✓ Documentation completeness > 80%

### Quality Gates
- ✓ All identified code smells addressed
- ✓ Architecture diagrams validated
- ✓ Refactored code peer-reviewed
- ✓ Modernization strategy approved
- ✓ Final report complete and reviewed

---

## Risks & Mitigation

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| **Schedule slippage** | Medium | Medium | Regular status updates, buffer time |
| **Missing requirements** | High | Low | Comprehensive analysis in Phase 1 |
| **Code complexity** | High | Medium | Iterative approach, incremental refactoring |
| **Team availability** | Medium | Low | Clear role definition, knowledge sharing |
| **Legacy system brittleness** | High | Medium | Comprehensive testing, version control |

---

## Budget & Resources

### Estimated Effort
- **Total Duration**: 14 weeks
- **Team Size**: 3-4 people
- **Total Effort**: ~500-600 person-hours

### Resource Requirements
- Development environment setup
- Analysis tools licenses (optional)
- Documentation and collaboration tools
- Version control infrastructure

---

## Conclusion

The Central Airport Management System is an ideal candidate for architecture recovery and re-engineering due to its complexity, technical debt, and real-world significance. This project will result in:

1. Better understanding of system architecture
2. Improved code quality and maintainability
3. Clear modernization pathway
4. Documentation for future development
5. Foundation for continuous improvement

The systematic approach through 5 phases ensures comprehensive analysis and practical improvements while minimizing risk to system stability.

---

**Document Version**: 1.0
**Date**: June 2026
**Status**: Active
