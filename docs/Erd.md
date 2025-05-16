| Table   | Column    | Type         | PK | FK | Not Null | Description      |
|---------|-----------|--------------|----|----|----------|------------------|
| Friend  | id        | Integer(Auto)| ✔  |    | ✔        | Primary Key      |
|         | name      | Char(100)    |    |    | ✔        | 이름             |
|         | mail      | Email(200)   |    |    | ✔        | 이메일           |
|         | age       | Integer      |    |    | ✔        | 나이             |
|         | birthday  | Date         |    |    | ✔        | 생일             |