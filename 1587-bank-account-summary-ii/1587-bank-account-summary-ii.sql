# Write your MySQL query statement below

SELECT u.name, t.balance
FROM users u, 
    ( SELECT account, sum(amount) as balance
    FROM Transactions
    GROUP BY account
    HAVING balance > 10000) t
WHERE u.account =t.account 
