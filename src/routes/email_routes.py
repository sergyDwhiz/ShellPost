from flask import Blueprint, request, jsonify
from models.email_classifier import classify_email
from models.email_model import Email
from utils.db import db
from email_sender import send_email, receive_emails

email_bp = Blueprint('email', __name__)

@email_bp.route('/emails', methods=['POST'])
def add_email():
    try:
        data = request.get_json()
        content = data.get('content')
        classification = classify_email(content)
        new_email = Email(content=content, classification=classification)
        db.session.add(new_email)
        db.session.commit()
        return jsonify({'id': new_email.id, 'content': new_email.content, 'classification': new_email.classification}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@email_bp.route('/emails', methods=['GET'])
def get_emails():
    try:
        emails = Email.query.all()
        return jsonify([{'id': email.id, 'content': email.content, 'classification': email.classification} for email in emails])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@email_bp.route('/send-email', methods=['POST'])
def send_email_endpoint():
    try:
        data = request.get_json()
        recipient = data.get('recipient')
        subject = data.get('subject')
        body = data.get('body')
        attachment_path = data.get('attachment_path')
        send_email(recipient, subject, body, attachment_path)
        return jsonify({'message': 'Email sent successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@email_bp.route('/receive-emails', methods=['GET'])
def receive_emails_endpoint():
    try:
        emails = receive_emails()
        return jsonify(emails), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500