# Code Analysis Plan - AMS Re-Engineering Project

## Overview
This document outlines the comprehensive plan for analyzing the Central Airport Management System (AMS) source code.

---

## 1. Program Comprehension

### 1.1 Source Code Structure Analysis
**Objective**: Understand the organization and structure of source code

**Tasks**:
- [ ] Count total files and lines of code (LOC)
- [ ] Identify programming languages used
- [ ] Map file-to-module relationships
- [ ] Create folder structure diagram
- [ ] Document file purposes and responsibilities

**Deliverables**:
- Source code statistics report
- Folder structure documentation
- File-to-function mapping

### 1.2 System Architecture Analysis
**Objective**: Identify system components and their interactions

**Tasks**:
- [ ] Extract main modules/components
- [ ] Document module responsibilities
- [ ] Identify module interactions
- [ ] Create dependency graph
- [ ] Analyze data flow between modules

**Deliverables**:
- Component diagram
- Dependency graph
- Data flow documentation

### 1.3 Database Schema Analysis
**Objective**: Understand data structure and relationships

**Tasks**:
- [ ] Extract all table definitions
- [ ] Document table relationships
- [ ] Identify primary and foreign keys
- [ ] Analyze schema normalization
- [ ] Create Entity-Relationship Diagram (ERD)

**Deliverables**:
- Database schema documentation
- ERD diagram
- Normalization analysis report

### 1.4 External Dependencies
**Objective**: Identify and document external libraries and services

**Tasks**:
- [ ] Extract import statements
- [ ] Identify third-party libraries
- [ ] Document library versions
- [ ] Identify external services
- [ ] Map version compatibility

**Deliverables**:
- Dependencies list
- Version compatibility report
- External services mapping

---

## 2. Reverse Engineering & Architecture Recovery

### 2.1 Logical Architecture
**Objective**: Recover the logical design of the system

**Tasks**:
- [ ] Identify architectural layers
- [ ] Extract design patterns used
- [ ] Document component interactions
- [ ] Create logical view diagrams
- [ ] Identify architectural violations

**Deliverables**:
- Logical architecture diagram
- Design patterns report
- Component responsibility document

### 2.2 Physical Architecture
**Objective**: Document deployment and infrastructure

**Tasks**:
- [ ] Identify runtime components
- [ ] Document deployment topology
- [ ] Map technology stack
- [ ] Identify performance bottlenecks
- [ ] Create deployment diagram

**Deliverables**:
- Physical architecture diagram
- Technology stack documentation
- Deployment topology diagram

### 2.3 Process View
**Objective**: Document key business processes

**Tasks**:
- [ ] Identify critical workflows
- [ ] Create sequence diagrams
- [ ] Document data transformations
- [ ] Identify process bottlenecks
- [ ] Create process flow diagrams

**Deliverables**:
- Sequence diagrams
- Process flow documentation
- Workflow analysis report

---

## 3. Static Code Analysis

### 3.1 Complexity Metrics
**Objective**: Measure code complexity

**Metrics to Collect**:
- **Cyclomatic Complexity (CC)**
  - Target: < 10 per function
  - Current expected: 15-25 (high)
  
- **Lines of Code (LOC)**
  - Per function
  - Per class/module
  - Total system

- **Depth of Nesting**
  - Target: < 3 levels
  - Current expected: 4-6 (high)

**Tools**: Radon, Pylint

**Deliverables**:
- Complexity metrics report
- High complexity functions list
- Complexity trend analysis

### 3.2 Coupling & Cohesion
**Objective**: Measure module interdependencies

**Metrics**:
- **Coupling Between Objects (CBO)**
  - Count dependencies per module
  - Identify tightly coupled pairs
  - Target: < 5 dependencies

- **Lack of Cohesion of Methods (LCOM)**
  - Measure method relationships
  - Identify god classes
  - Target: > 0.8 cohesion

- **Afferent/Efferent Coupling**
  - Incoming dependencies
  - Outgoing dependencies
  - Balance analysis

**Tools**: SonarQube, CodeClimate

**Deliverables**:
- Coupling analysis report
- Dependency matrix
- Cohesion assessment

### 3.3 Code Quality Issues
**Objective**: Identify and categorize quality problems

**Checks**:
- [ ] **Naming Conventions**
  - Variable names clarity
  - Function/method naming
  - Class naming consistency

- [ ] **Documentation**
  - Missing docstrings
  - Outdated comments
  - API documentation gaps

- [ ] **Error Handling**
  - Uncaught exceptions
  - Silent failures
  - Incomplete error messages

- [ ] **Performance Issues**
  - O(n²) algorithms
  - Inefficient queries
  - Memory leaks

- [ ] **Security Issues**
  - SQL injection risks
  - Input validation gaps
  - Access control issues

**Tools**: SonarQube, Pylint, Bandit

**Deliverables**:
- Quality issues report (prioritized)
- Security vulnerabilities list
- Performance problems document

### 3.4 Code Smell Detection
**Objective**: Identify design problems and anti-patterns

**Code Smells to Detect**:
- [ ] **God Classes/Methods**
  - Functions > 50 LOC
  - Classes > 500 LOC
  - Multiple responsibilities

- [ ] **Duplicate Code**
  - Copy-paste code
  - Similar implementations
  - Target: < 5% duplication

- [ ] **Long Parameter Lists**
  - Functions > 4 parameters
  - Constructor > 5 parameters

- [ ] **Feature Envy**
  - Methods using other class data
  - Tight coupling indicators

- [ ] **Data Clumps**
  - Frequently used data groups
  - Refactoring candidates

**Tools**: Pylint, CodeClimate, SonarQube

**Deliverables**:
- Code smell catalog
- Severity classification
- Refactoring recommendations

---

## 4. Code Quality Metrics

### 4.1 Metrics to Measure

| Metric | Tool | Target | Category |
|--------|------|--------|----------|
| **Cyclomatic Complexity** | Radon | < 10 | Complexity |
| **Lines of Code** | Radon | < 100/function | Size |
| **Coupling Between Objects** | SonarQube | < 5 | Coupling |
| **Lack of Cohesion** | SonarQube | > 0.8 | Cohesion |
| **Code Duplication** | SonarQube | < 5% | Duplication |
| **Test Coverage** | Coverage.py | > 60% | Testing |
| **Maintainability Index** | Radon | > 70 | Maintainability |
| **Technical Debt** | SonarQube | < 10% | Quality |
| **Documentation %** | Pylint | > 80% | Documentation |
| **Bug Density** | SonarQube | < 1 bug/1000 LOC | Defects |

### 4.2 Metrics Collection
**Process**:
1. Run static analysis tools
2. Collect metrics data
3. Normalize data
4. Compare against benchmarks
5. Identify outliers
6. Generate reports

**Tools**:
- Radon (LOC, complexity)
- Pylint (style, quality)
- SonarQube (comprehensive)
- Coverage.py (test coverage)

---

## 5. Identification of Issues

### 5.1 Architecture-Level Issues
- [ ] Monolithic design
- [ ] Tight coupling between layers
- [ ] Missing abstraction layers
- [ ] Circular dependencies
- [ ] Scalability limitations

### 5.2 Design-Level Issues
- [ ] Missing design patterns
- [ ] Inconsistent design
- [ ] Poor separation of concerns
- [ ] Violation of SOLID principles

### 5.3 Code-Level Issues
- [ ] Code smells (cataloged above)
- [ ] Anti-patterns
- [ ] Performance issues
- [ ] Security vulnerabilities

### 5.4 Documentation Issues
- [ ] Outdated documentation
- [ ] Missing API documentation
- [ ] Incomplete comments
- [ ] No architecture documentation

---

## 6. Analysis Methodology

### 6.1 Cyclomatic Complexity Analysis

**Formula**: CC = Number of decision points + 1

**Classification**:
- 1-5: Simple, low risk
- 6-10: Moderate complexity, some risk
- 11-20: Complex, high risk
- 20+: Very complex, very high risk

**Actions**:
- CC 1-5: No changes needed
- CC 6-10: Monitor, consider refactoring
- CC 11-20: Refactor (high priority)
- CC 20+: Refactor (critical priority)

### 6.2 Coupling Analysis

**Calculate Afferent Coupling (Ca)**:
- Number of classes depending on this class

**Calculate Efferent Coupling (Ce)**:
- Number of classes this class depends on

**Instability** = Ce / (Ca + Ce)
- 0 = Stable
- 1 = Unstable

**Target**: Keep instability between 0.3-0.7

### 6.3 Code Duplication Detection

**Process**:
1. Extract all code blocks
2. Hash blocks for comparison
3. Identify identical blocks
4. Calculate duplication percentage
5. Rank by impact

---

## 7. Deliverables Schedule

| Phase | Deliverable | Due Date | Status |
|-------|-------------|----------|--------|
| 1 | Program Comprehension Report | Week 2 | Pending |
| 2 | Architecture Recovery Diagrams | Week 5 | Pending |
| 3 | Code Analysis Report | Week 8 | Pending |
| 3 | Metrics Report | Week 8 | Pending |
| 4 | Refactored Code Samples | Week 12 | Pending |
| 5 | Modernization Strategy | Week 14 | Pending |
| 5 | Final Technical Report | Week 14 | Pending |

---

## 8. Quality Assurance

### 8.1 Analysis Validation
- [ ] Multiple tool cross-validation
- [ ] Manual code review sampling (10%)
- [ ] Peer review of findings
- [ ] Stakeholder validation

### 8.2 Report Accuracy
- [ ] Data consistency checks
- [ ] Outlier investigation
- [ ] Tool output verification
- [ ] Documentation review

---

## 9. Risk Management

### 9.1 Analysis Risks
- **Incomplete code coverage**: Mitigation - Use multiple tools
- **False positives**: Mitigation - Manual validation
- **Tool limitations**: Mitigation - Multi-tool approach
- **Dependency changes**: Mitigation - Version pinning

### 9.2 Mitigation Strategies
1. Use multiple analysis tools
2. Manual verification of findings
3. Peer review process
4. Documentation of assumptions
5. Regular progress tracking

---

## 10. References

### Standards
- ISO/IEC 9126 - Software quality characteristics
- IEEE 1061 - Software quality metrics
- OWASP - Security vulnerability guidelines

### Tools Documentation
- [Pylint Documentation](https://pylint.pycqa.org/)
- [Radon Documentation](https://radon.readthedocs.io/)
- [SonarQube Documentation](https://docs.sonarqube.org/)
- [Coverage.py Documentation](https://coverage.readthedocs.io/)

---

**Document Version**: 1.0
**Last Updated**: June 2026
**Status**: Active
