# HAC API

## Introduction

This is a simple API to access the Home Access Center (HAC) of the [Frisco Independent School District](https://www.friscoisd.org/). This API is not affiliated with the school district in any way.

---

## Modules

### assignment_grades

* return_quarter_assignments_html(***quarter***)
* return_quarter_assignments_df(***quarter***)
* return_current_assignments_df(    )
* return_current_assignments_html(  )

### course_grades

* return_current_grades(  )
* return_quarter_grade(***quarter***)

### session

* init(***username***, ***password***)
* reset(    )
* return_to_current(    )

### transcript

* return_weighted_gpa(  )
* return_college_gpa(   )

### misc

* is_updated(***original***, ***new***)
* get_time( )

---
