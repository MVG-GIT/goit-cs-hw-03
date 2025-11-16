-- отримати всі завдання певного користувача (user_id = 3)
SELECT * FROM tasks WHERE user_id = 3;

-- вибрати завдання за певним статусом (new)
SELECT * FROM tasks
WHERE status_id = (SELECT id FROM status WHERE name = 'new');

-- оновити статус конкретного завдання (id = 5 → in progress)
UPDATE tasks
SET status_id = (SELECT id FROM status WHERE name = 'in progress')
WHERE id = 5;

-- отримати список користувачів які не мають жодного завдання
SELECT * FROM users
WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);

-- додати нове завдання для конкретного користувача
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('New important task', 'This is a manually added task.',
        (SELECT id FROM status WHERE name = 'new'), 2);

-- отримати всі завдання які ще не завершено
SELECT * FROM tasks
WHERE status_id != (SELECT id FROM status WHERE name = 'completed');

-- видалити конкретне завдання
DELETE FROM tasks WHERE id = 10;

-- знайти користувачів з певною електронною поштою
SELECT * FROM users WHERE email LIKE '%@gmail.com%';

-- оновити ім'я користувача
UPDATE users SET fullname = 'Updated User Name' WHERE id = 4;

-- отримати кількість завдань для кожного статусу
SELECT s.name AS status, COUNT(t.id) AS task_count
FROM status s
LEFT JOIN tasks t ON s.id = t.status_id
GROUP BY s.name;

-- отримати завдання які призначені користувачам з певним доменом
SELECT t.* FROM tasks t
JOIN users u ON t.user_id = u.id
WHERE u.email LIKE '%@example.com%';

-- отримати список завдань, що не мають опису
SELECT * FROM tasks WHERE description IS NULL;

-- вибрати користувачів та їхні завдання у статусі in progress
SELECT u.fullname, t.title
FROM users u
JOIN tasks t ON u.id = t.user_id
JOIN status s ON s.id = t.status_id
WHERE s.name = 'in progress';

-- отримати користувачів та кількість їхніх завдань
SELECT u.fullname, COUNT(t.id) AS task_count
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.fullname
ORDER BY task_count DESC;
