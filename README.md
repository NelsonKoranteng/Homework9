# Homework-9
1. Clone this repository.
2. Run your Django server.

```bash
python manage.py runserver
```

3. It would complain about missing Django installation. Please set the environment and install Django.
4. Go to the root folder and create a new env.
5. Then activate the env.
6. Install Django and then run the server.
8. Try [http://localhost:8080/security/unsafe/users/1](http://localhost:8080/security/unsafe/users/1)
9. It should show:

> User 1 test

1. Now try [http://localhost:8080/security/unsafe/users/1 or 1](http://localhost:8080/security/unsafe/users/1%20or%201)
2. You will see all the users in the system.

> User 1 testUser 2 test2User 3 test3

1. Your challenge is to fix the project and make sure the following SQL injection won't return any data: [http://localhost:8080/security/unsafe/users/1 or 1](http://localhost:8080/security/unsafe/users/1%20or%201).

Tip: Check the following site and apply the security fix suggested [https://lchsk.com/stay-paranoid-and-trust-no-one-overview-of-common-security-vulnerabilities-in-web-applications.html](https://lchsk.com/stay-paranoid-and-trust-no-one-overview-of-common-security-vulnerabilities-in-web-applications.html)
check archive:[https://web.archive.org/web/20210228214306/https://lchsk.com/stay-paranoid-and-trust-no-one-overview-of-common-security-vulnerabilities-in-web-applications.html]
