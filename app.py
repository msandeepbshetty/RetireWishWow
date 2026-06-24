"""
RetireWishWow - Flask Backend Server
Handles contact form submissions and sends emails
Author: RetireWishWow Team
Date: 2024
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os
import re
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Enable CORS (Cross-Origin Resource Sharing) for frontend communication
CORS(app)

# ==========================================
# CONFIGURATION
# ==========================================

# Email configuration - Update these with your email credentials
EMAIL_SENDER = os.getenv('EMAIL_SENDER', 'your_email@gmail.com')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', 'your_app_password')
EMAIL_RECIPIENT = os.getenv('EMAIL_RECIPIENT', 'msandeepbshetty@outlook.com')
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))

# ==========================================
# UTILITY FUNCTIONS
# ==========================================

def validate_email(email):
    """
    Validate email format
    Args:
        email (str): Email address to validate
    Returns:
        bool: True if valid, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_form_data(data):
    """
    Validate contact form data
    Args:
        data (dict): Form data to validate
    Returns:
        tuple: (is_valid, error_message)
    """
    # Check required fields
    required_fields = ['name', 'email', 'subject', 'message']
    for field in required_fields:
        if field not in data or not data[field].strip():
            return False, f"Missing required field: {field}"
    
    # Validate email format
    if not validate_email(data['email']):
        return False, "Invalid email address format"
    
    # Check field lengths
    if len(data['name']) > 100:
        return False, "Name is too long (max 100 characters)"
    
    if len(data['subject']) > 200:
        return False, "Subject is too long (max 200 characters)"
    
    if len(data['message']) > 5000:
        return False, "Message is too long (max 5000 characters)"
    
    return True, None


def create_email_body(form_data):
    """
    Create HTML email body with form data
    Args:
        form_data (dict): Contact form data
    Returns:
        str: HTML formatted email body
    """
    html_body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; background-color: #f5f5f5; }}
            .header {{ background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%); color: white; padding: 20px; border-radius: 5px 5px 0 0; text-align: center; }}
            .content {{ background-color: white; padding: 30px; }}
            .field {{ margin-bottom: 20px; }}
            .label {{ font-weight: bold; color: #2c3e50; margin-bottom: 5px; }}
            .value {{ background-color: #f0f0f0; padding: 10px; border-radius: 3px; border-left: 4px solid #3498db; }}
            .footer {{ background-color: #f0f0f0; padding: 15px; text-align: center; font-size: 12px; color: #666; border-radius: 0 0 5px 5px; }}
            .timestamp {{ color: #999; font-size: 12px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🌍 RetireWishWow - New Contact Form Submission</h1>
            </div>
            <div class="content">
                <div class="field">
                    <div class="label">Name:</div>
                    <div class="value">{form_data.get('name', 'N/A')}</div>
                </div>
                
                <div class="field">
                    <div class="label">Email:</div>
                    <div class="value"><a href="mailto:{form_data.get('email', 'N/A')}">{form_data.get('email', 'N/A')}</a></div>
                </div>
                
                <div class="field">
                    <div class="label">Phone:</div>
                    <div class="value">{form_data.get('phone', 'Not provided') or 'Not provided'}</div>
                </div>
                
                <div class="field">
                    <div class="label">Subject:</div>
                    <div class="value">{form_data.get('subject', 'N/A')}</div>
                </div>
                
                <div class="field">
                    <div class="label">Message:</div>
                    <div class="value">{form_data.get('message', 'N/A')}</div>
                </div>
            </div>
            <div class="footer">
                <p>Submitted on: <span class="timestamp">{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</span></p>
                <p>&copy; 2024 RetireWishWow. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html_body


def send_email(recipient_email, subject, html_body):
    """
    Send email via SMTP
    Args:
        recipient_email (str): Recipient email address
        subject (str): Email subject
        html_body (str): HTML formatted email body
    Returns:
        tuple: (success, message)
    """
    try:
        # Create email message
        message = MIMEMultipart('alternative')
        message['Subject'] = subject
        message['From'] = EMAIL_SENDER
        message['To'] = recipient_email
        
        # Attach HTML content
        html_part = MIMEText(html_body, 'html')
        message.attach(html_part)
        
        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable TLS encryption
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(message)
        
        return True, "Email sent successfully"
    
    except smtplib.SMTPAuthenticationError:
        return False, "SMTP authentication failed. Check email and password."
    except smtplib.SMTPException as e:
        return False, f"SMTP error occurred: {str(e)}"
    except Exception as e:
        return False, f"Error sending email: {str(e)}"


# ==========================================
# ROUTES
# ==========================================

@app.route('/')
def index():
    """
    Root route - returns welcome message
    """
    return jsonify({
        'message': 'RetireWishWow Backend Server',
        'status': 'Running',
        'version': '1.0.0',
        'endpoints': {
            'send_email': 'POST /send-email',
            'health_check': 'GET /health'
        }
    }), 200


@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint - verifies server status
    """
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    }), 200


@app.route('/send-email', methods=['POST'])
def send_contact_email():
    """
    Handle contact form submission and send email
    Expected JSON payload:
    {
        "name": "string",
        "email": "string",
        "phone": "string (optional)",
        "subject": "string",
        "message": "string"
    }
    Returns:
        JSON response with status and message
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'message': 'No data provided'
            }), 400
        
        # Validate form data
        is_valid, error_message = validate_form_data(data)
        if not is_valid:
            return jsonify({
                'success': False,
                'message': error_message
            }), 400
        
        # Create email subject with name
        email_subject = f"RetireWishWow - New Contact Form: {data.get('subject', 'No Subject')}"
        
        # Create HTML email body
        html_body = create_email_body(data)
        
        # Send email to admin
        success, message = send_email(EMAIL_RECIPIENT, email_subject, html_body)
        
        if not success:
            return jsonify({
                'success': False,
                'message': message
            }), 500
        
        # Optional: Send confirmation email to user
        # Uncomment below to enable auto-reply to user
        # user_subject = "RetireWishWow - We Received Your Message"
        # user_body = f"""
        # <html><body>
        # <p>Dear {data.get('name')},</p>
        # <p>Thank you for contacting RetireWishWow! We have received your message and will get back to you shortly.</p>
        # <p>Best regards,<br/>The RetireWishWow Team</p>
        # </body></html>
        # """
        # send_email(data.get('email'), user_subject, user_body)
        
        return jsonify({
            'success': True,
            'message': 'Your message has been sent successfully! We will get back to you soon.'
        }), 200
    
    except Exception as e:
        print(f"Unexpected error in send_contact_email: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'An unexpected error occurred. Please try again later.'
        }), 500


@app.route('/test-email', methods=['POST'])
def test_email():
    """
    Test email endpoint - sends a test email to verify configuration
    Requires email_address in JSON body
    """
    try:
        data = request.get_json()
        test_email_address = data.get('email_address', EMAIL_RECIPIENT)
        
        # Validate email
        if not validate_email(test_email_address):
            return jsonify({
                'success': False,
                'message': 'Invalid email address'
            }), 400
        
        # Create test email
        test_html = """
        <!DOCTYPE html>
        <html>
        <body style="font-family: Arial, sans-serif;">
            <h2>RetireWishWow - Test Email</h2>
            <p>Hello!</p>
            <p>This is a test email to verify that the RetireWishWow email system is working correctly.</p>
            <p><strong>Test Status:</strong> ✅ Email Configuration is Working!</p>
            <p>Best regards,<br/>RetireWishWow Team</p>
        </body>
        </html>
        """
        
        success, message = send_email(test_email_address, "RetireWishWow - Test Email", test_html)
        
        return jsonify({
            'success': success,
            'message': message
        }), 200 if success else 500
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error: {str(e)}'
        }), 500


# ==========================================
# ERROR HANDLERS
# ==========================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'success': False,
        'message': 'Endpoint not found',
        'error': str(error)
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'success': False,
        'message': 'Internal server error',
        'error': str(error)
    }), 500


# ==========================================
# MAIN
# ==========================================

if __name__ == '__main__':
    # Print startup information
    print("=" * 60)
    print("RetireWishWow - Backend Server Starting")
    print("=" * 60)
    print(f"Email Configuration:")
    print(f"  SMTP Server: {SMTP_SERVER}")
    print(f"  SMTP Port: {SMTP_PORT}")
    print(f"  Sender Email: {EMAIL_SENDER}")
    print(f"  Recipient Email: {EMAIL_RECIPIENT}")
    print("=" * 60)
    print("Server running on: http://127.0.0.1:5000")
    print("=" * 60)
    
    # Run Flask app
    # Set debug=False for production
    app.run(debug=True, host='127.0.0.1', port=5000)
