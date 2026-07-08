import os
import tempfile
import unittest

from app import app, init_db


class AttendanceSystemTests(unittest.TestCase):
    def setUp(self):
        self.db_fd, self.db_path = tempfile.mkstemp()
        app.config.update(TESTING=True, DATABASE=self.db_path)
        with app.app_context():
            init_db()
        self.client = app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.db_path)

    def test_index_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Attendance System", response.data)

    def test_register_and_login_flow(self):
        response = self.client.post(
            "/register",
            data={
                "username": "alice",
                "email": "alice@example.com",
                "password": "secret123",
                "confirm_password": "secret123",
            },
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Please log in", response.data)

        login_response = self.client.post(
            "/login",
            data={"username": "alice", "password": "secret123"},
            follow_redirects=True,
        )
        self.assertEqual(login_response.status_code, 200)
        self.assertIn(b"Welcome back!", login_response.data)

    def test_attendance_and_help_request_flow(self):
        self.client.post(
            "/register",
            data={
                "username": "bob",
                "email": "bob@example.com",
                "password": "secret123",
                "confirm_password": "secret123",
            },
        )
        self.client.post(
            "/login",
            data={"username": "bob", "password": "secret123"},
        )

        attendance_response = self.client.post(
            "/attendance",
            data={
                "employee_name": "Jane Doe",
                "attendance_date": "2026-07-08",
                "status": "Present",
                "department": "Operations",
                "notes": "On time",
            },
            follow_redirects=True,
        )
        self.assertEqual(attendance_response.status_code, 200)
        self.assertIn(b"Attendance recorded successfully", attendance_response.data)

        help_response = self.client.post(
            "/help",
            data={"subject": "Login issue", "message": "I cannot access the dashboard."},
            follow_redirects=True,
        )
        self.assertEqual(help_response.status_code, 200)
        self.assertIn(b"Your help request has been submitted", help_response.data)


if __name__ == "__main__":
    unittest.main()
