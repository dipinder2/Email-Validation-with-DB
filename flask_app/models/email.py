from ..config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class Email:
    def __init__(self,data):
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def add_email(cls,data):
        q = '''
            INSERT INTO emails(email)
            VALUES(%(email)s);
        '''
        return connectToMySQL("email_schema").query_db(q, data)
    
    
    @classmethod
    def get_all_emails(cls):
        q = '''
        SELECT * FROM emails;
        '''
        results = connectToMySQL("email_schema").query_db(q)
        emails = []
        for res in results:
            emails.append(cls(res))
        return emails
    
    
    @classmethod
    def delete_email(cls,data):
        q = '''
            DELETE FROM emails WHERE id = %(id)s
        '''
        return connectToMySQL("email_schema").query_db(q, data)
        
        
    @staticmethod
    def validate(user):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid