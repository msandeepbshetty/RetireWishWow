# RetireWishWow - Complete Website for Retirement Planning

A modern, responsive website helping people plan retirement in affordable countries worldwide.

## 📋 Project Overview

**RetireWishWow** is a comprehensive platform that assists retirees and pre-retirees in planning their retirement abroad. The website provides:

- 🏠 **Low-Cost Accommodation Options** - Find affordable housing in retirement destinations
- 🏥 **Health & Travel Insurance** - Secure coverage for international retirees
- 📋 **Long-Stay Visas** - Navigate visa requirements for various countries
- ✈️ **Travel Planning** - Detailed relocation guides and checklists
- 👴 **Old-Age Care Services** - Quality senior care at affordable prices
- 💰 **Cost-of-Living Guidance** - Detailed expense breakdowns and budget tools

## 🎯 Key Features

✅ **Modern, Clean Design** - Professional appearance with excellent UX
✅ **Fully Responsive** - Works perfectly on desktop, tablet, and mobile
✅ **Contact Form** - Email integration for customer inquiries
✅ **Fast Performance** - Optimized for quick loading
✅ **Accessible** - Follows accessibility best practices
✅ **SEO Friendly** - Structured HTML for search engines
✅ **Backend Integration** - Python Flask server with email functionality

## 📁 Project Structure

```
RetireWishWow/
├── index.html          # Home page with features and destinations
├── about.html          # About Us page with mission and team
├── contact.html        # Contact page with inquiry form
├── styles.css          # Complete stylesheet with responsive design
├── app.py              # Flask backend for email handling
├── requirements.txt    # Python dependencies
├── .env.template       # Environment variables template
└── README.md           # This file
```

## 🌐 Pages Included

### 1. **Home Page** (`index.html`)
- Hero section with tagline: "Retire Smart. Retire Abroad. Retire Wow."
- Mission statement
- Six feature cards covering all services
- Popular retirement destinations showcase
- Call-to-action section
- Footer with links and contact info

### 2. **About Us Page** (`about.html`)
- Company mission and vision
- Why RetireWishWow was created
- Core values (Honesty, Accuracy, Community, Empowerment, etc.)
- What sets the company apart
- Team member profiles
- Call-to-action

### 3. **Contact Page** (`contact.html`)
- Contact form with fields:
  - Name (required)
  - Email (required)
  - Phone (optional)
  - Subject (required)
  - Message (required)
- Contact information section
- FAQ section with 6 common questions
- Real-time form validation
- Success/error messages

## 🎨 Design Features

- **Color Scheme**: Professional blues, grays, and accents
- **Typography**: Clean, modern fonts (Segoe UI, sans-serif)
- **Layout**: Grid-based responsive design
- **Animations**: Smooth transitions and hover effects
- **Mobile First**: Optimized for all screen sizes

### Responsive Breakpoints
- Desktop: 1200px+
- Tablet: 768px - 1199px
- Mobile: Below 768px
- Small Mobile: Below 480px

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- A Gmail or Outlook account for email sending

### Installation

1. **Clone the repository** (or download files)
```bash
git clone https://github.com/msandeepbshetty/RetireWishWow.git
cd RetireWishWow
```

2. **Install Python dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure email settings**
   - Copy `.env.template` to `.env`
   - Edit `.env` and add your email credentials

```bash
cp .env.template .env
```

Edit `.env`:
```
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password_here
EMAIL_RECIPIENT=msandeepbshetty@outlook.com
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

### Running the Backend

1. **Start the Flask server**
```bash
python app.py
```

The server will start at `http://127.0.0.1:5000`

Expected output:
```
============================================================
RetireWishWow - Backend Server Starting
============================================================
Email Configuration:
  SMTP Server: smtp.gmail.com
  SMTP Port: 587
  Sender Email: your_email@gmail.com
  Recipient Email: msandeepbshetty@outlook.com
============================================================
Server running on: http://127.0.0.1:5000
============================================================
```

2. **Access the website**
   - Open `index.html` in your browser locally, or
   - Host the HTML files on a web server
   - The backend API will be available at `http://127.0.0.1:5000`

## 📧 Email Configuration Guide

### Using Gmail

1. **Enable 2-Step Verification**
   - Go to https://myaccount.google.com/security
   - Click "2-Step Verification"
   - Follow the setup process

2. **Generate App Password**
   - Visit https://myaccount.google.com/apppasswords
   - Select "Mail" and "Windows Computer" (or your device)
   - Google will generate a 16-character password
   - Use this password in `.env` as `EMAIL_PASSWORD`

3. **Update `.env`**
```
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=xxxx xxxx xxxx xxxx  (the 16-char password from step 2)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

### Using Outlook

1. **Allow less secure app access** (if needed)
2. **Update `.env`**
```
EMAIL_SENDER=your_email@outlook.com
EMAIL_PASSWORD=your_outlook_password
SMTP_SERVER=smtp-mail.outlook.com
SMTP_PORT=587
```

## 🔌 API Endpoints

### 1. Send Contact Email
**Endpoint:** `POST /send-email`

**Request Body:**
```json
{
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "+1-555-123-4567",
    "subject": "Inquiry about Mexico retirement",
    "message": "I would like to know more about retiring in Mexico..."
}
```

**Success Response (200):**
```json
{
    "success": true,
    "message": "Your message has been sent successfully! We will get back to you soon."
}
```

**Error Response (400):**
```json
{
    "success": false,
    "message": "Missing required field: email"
}
```

### 2. Health Check
**Endpoint:** `GET /health`

**Response:**
```json
{
    "status": "healthy",
    "timestamp": "2024-06-24T15:30:00.000000"
}
```

### 3. Server Info
**Endpoint:** `GET /`

**Response:**
```json
{
    "message": "RetireWishWow Backend Server",
    "status": "Running",
    "version": "1.0.0",
    "endpoints": {
        "send_email": "POST /send-email",
        "health_check": "GET /health"
    }
}
```

### 4. Test Email (Optional)
**Endpoint:** `POST /test-email`

**Request Body:**
```json
{
    "email_address": "test@example.com"
}
```

## 🔒 Security Features

- **Input Validation**: All form fields are validated before processing
- **Email Validation**: RFC-compliant email format checking
- **Field Length Limits**: Prevents database abuse
  - Name: max 100 characters
  - Subject: max 200 characters
  - Message: max 5000 characters
- **CORS Enabled**: Allows frontend and backend communication
- **Error Handling**: Graceful error responses without exposing system details
- **SMTP Security**: TLS encryption for email transmission

## 📱 Responsive Design

The website is fully responsive with breakpoints for:
- **Large Screens** (1200px+): Full desktop layout with all features
- **Tablets** (768-1199px): Optimized grid layouts
- **Mobile Phones** (below 768px): Single-column layout
- **Small Mobile** (below 480px): Compact design with adjusted fonts

## 🧪 Testing

### Test the Frontend
1. Open `index.html`, `about.html`, or `contact.html` in a browser
2. Test responsiveness using browser DevTools (F12)
3. Navigate between pages
4. Test form validation on contact page

### Test the Backend
1. Start the Flask server: `python app.py`
2. Test with curl or Postman:

```bash
# Test health check
curl http://127.0.0.1:5000/health

# Test contact form
curl -X POST http://127.0.0.1:5000/send-email \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test User",
    "email": "test@example.com",
    "subject": "Test Subject",
    "message": "This is a test message"
  }'
```

## 🚀 Deployment

### Hosting the Frontend
- Upload HTML, CSS files to any web hosting service
- Popular options: GitHub Pages, Netlify, Vercel, AWS S3

### Hosting the Backend
- **Heroku**: Free tier available (may be limited)
- **PythonAnywhere**: Easy Python hosting
- **AWS EC2**: Full control and scalability
- **DigitalOcean**: Affordable VPS hosting
- **Render**: Modern cloud platform for Python apps

### Production Checklist
- [ ] Set `debug=False` in `app.py`
- [ ] Use environment variables for all credentials
- [ ] Enable HTTPS/SSL
- [ ] Configure CORS properly for your domain
- [ ] Set up error logging and monitoring
- [ ] Use a production WSGI server (Gunicorn, uWSGI)
- [ ] Test all functionality thoroughly

## 🛠️ Customization

### Change Colors
Edit CSS variables in `styles.css`:
```css
:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --accent-color: #e74c3c;
    /* ... more colors ... */
}
```

### Update Contact Recipients
Edit `.env`:
```
EMAIL_RECIPIENT=your_email@yourdomain.com
```

### Add More Pages
1. Create new HTML file based on existing structure
2. Include same navigation and footer
3. Link from other pages

## 📝 Code Comments

All code includes inline comments explaining:
- Function purposes
- Parameter descriptions
- Complex logic sections
- Configuration options

## 🤝 Support & Maintenance

### Common Issues

**Issue**: "SMTP authentication failed"
- **Solution**: Verify email and password in `.env`
- Check if Gmail App Password is correctly generated

**Issue**: "Module not found: Flask"
- **Solution**: Run `pip install -r requirements.txt`

**Issue**: Form not submitting
- **Solution**: Check browser console for errors
- Verify backend server is running
- Check CORS settings

**Issue**: Website styling looks broken
- **Solution**: Clear browser cache (Ctrl+Shift+Delete)
- Verify `styles.css` is in the same directory as HTML files

## 📚 Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Backend**: Python 3.7+, Flask 2.3+
- **Email**: SMTP (Gmail/Outlook)
- **Styling**: CSS3 with CSS Variables
- **Design**: Responsive CSS Grid and Flexbox
- **Browser Support**: All modern browsers

## 📄 File Descriptions

| File | Purpose |
|------|---------|
| `index.html` | Home page with hero, features, destinations |
| `about.html` | Company mission, values, team information |
| `contact.html` | Contact form, info, FAQ |
| `styles.css` | All styling, responsive design, animations |
| `app.py` | Flask backend, email handling, validation |
| `requirements.txt` | Python package dependencies |
| `.env.template` | Environment variables template |
| `README.md` | This comprehensive documentation |

## 📞 Contact & Support

For questions or issues:
- Email: info@retirewishwow.com
- Website: www.retirewishwow.com

## 📄 License

This project is created for RetireWishWow. All rights reserved © 2024.

## 🎓 Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [CSS-Tricks](https://css-tricks.com/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [SMTP Documentation](https://tools.ietf.org/html/rfc5321)

---

**Happy Retiring! 🌍🏝️**

Version 1.0.0 | Last Updated: June 24, 2024
