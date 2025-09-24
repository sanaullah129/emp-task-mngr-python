# Employee Task Manager

A full-stack web application for managing employees and their tasks, featuring a FastAPI backend with PostgreSQL and a modern React frontend.

## 🚀 Quick Start

### Backend (FastAPI)
```bash
# Setup backend
python -m venv fastapi-env
source fastapi-env/bin/activate  # On Windows: fastapi-env\Scripts\activate
pip install -r requirements.txt
python init_db.py
uvicorn main:app --reload --port 8000
```

### Frontend (React)
```bash
# Setup frontend (in new terminal)
cd emp-task-mangr-client
npm install -g pnpm  # Install pnpm if not already installed
pnpm install
pnpm dev
```

**Access the application:**
- **Frontend**: http://localhost:5173 (React SPA)
- **Backend API**: http://localhost:8000 (FastAPI)
- **API Docs**: http://localhost:8000/docs (Swagger UI)

**Login credentials:** `admin` / `admin123`

---

## 🏗 Architecture

### Backend Features (FastAPI + PostgreSQL)
- **JWT Authentication**: Secure token-based authentication
- **Employee Management**: Complete CRUD operations for employee records
- **Task Management**: Task assignment, status tracking, and management
- **PostgreSQL Database**: Robust data storage with relationships
- **API Documentation**: Interactive Swagger UI documentation
- **Input Validation**: Comprehensive request validation using Pydantic
- **Error Handling**: Proper HTTP status codes and error messages

### Frontend Features (React + TypeScript + Material-UI)
- **Modern React SPA**: Built with React 19 and TypeScript
- **Material-UI Design**: Professional, responsive interface
- **Authentication**: JWT-based login with persistent sessions
- **Employee Dashboard**: Interactive cards for employee management
- **Task Dashboard**: Visual task tracking with status indicators
- **Real-time Updates**: Instant synchronization with backend API
- **Form Validation**: Client-side validation with error handling
- **Mobile Responsive**: Optimized for all device sizes

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.8 or higher** ([Download Python](https://www.python.org/downloads/))
- **Node.js 16 or higher** ([Download Node.js](https://nodejs.org/))
- **PostgreSQL** ([Download PostgreSQL](https://www.postgresql.org/download/))
- **PNPM** (`npm install -g pnpm`)
- **Git** (optional, for cloning)

## 🔧 Complete Setup Instructions

### Step 1: Project Setup

#### Option A: Clone with Git
```bash
git clone <repository-url>
cd employee-task-manager
```

#### Option B: Download and Extract
1. Download the project files
2. Extract to a folder called `employee-task-manager`
3. Navigate to the project directory

### Step 2: Backend Setup (FastAPI)

#### 2.1 Setup PostgreSQL Database

1. **Start PostgreSQL service:**
   ```bash
   # On macOS with Homebrew
   brew services start postgresql
   
   # On Ubuntu/Debian
   sudo service postgresql start
   
   # On Windows
   # Start PostgreSQL from Services or pgAdmin
   ```

2. **Create database:**
   ```bash
   # Connect to PostgreSQL
   psql -U postgres
   
   # Create database
   CREATE DATABASE employee_db;
   
   # Exit PostgreSQL
   \q
   ```

#### 2.2 Python Environment Setup

1. **Create and activate virtual environment:**
   ```bash
   # Create virtual environment
   python3 -m venv fastapi-env
   
   # Activate virtual environment
   # On macOS/Linux
   source fastapi-env/bin/activate
   
   # On Windows
   fastapi-env\Scripts\activate
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

#### 2.3 Environment Configuration

1. **Create `.env` file** in the project root directory:
   ```env
   DATABASE_URL=postgresql://postgres:postgres@localhost:5432/employee_db
   SECRET_KEY=your-super-secret-key-change-this-in-production
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

   > **Note:** Replace `postgres:postgres` with your PostgreSQL username and password if different.

#### 2.4 Initialize Database

```bash
python init_db.py
```

This will create all tables and seed with sample data.

#### 2.5 Start Backend Server

```bash
uvicorn main:app --reload --port 8000
```

Verify at: http://localhost:8000

### Step 3: Frontend Setup (React)

#### 3.1 Navigate to Client Directory

```bash
cd emp-task-mangr-client
```

#### 3.2 Install Dependencies

```bash
# Install PNPM if not already installed
npm install -g pnpm

# Install project dependencies
pnpm install
```

#### 3.3 Start Development Server

```bash
pnpm dev
```

The frontend will be available at: http://localhost:5173

### Step 4: Access the Application

1. **Open your browser** and navigate to: `http://localhost:5173`
2. **Login** with default credentials:
   - **Username**: `admin`
   - **Password**: `admin123`
3. **Explore the features:**
   - Employee management (create, read, update, delete)
   - Task management with status tracking
   - Responsive design on mobile and desktop

## 📱 Application Usage

### Frontend Application (React SPA)

Access the web application at **http://localhost:5173**

#### Features:
- **Dashboard Navigation**: Clean Material-UI interface
- **Employee Management**: 
  - View all employees in card layout
  - Add new employees with form validation
  - Edit existing employee details
  - Delete employees (with confirmation)
- **Task Management**:
  - Create new tasks and assign to employees
  - Visual status indicators (pending/ongoing/completed)
  - Update task status with one click
  - Due date management with date picker
  - Overdue task alerts
- **Authentication**: Secure login with persistent sessions

#### Available Scripts:
- `pnpm dev` - Start development server (port 5173)
- `pnpm build` - Build for production
- `pnpm preview` - Preview production build
- `pnpm lint` - Run ESLint

### Backend API (FastAPI)

Access the API at **http://localhost:8000**

#### Interactive Documentation:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Testing the API

### Option 1: Using the Interactive Documentation

1. Go to `http://localhost:8000/docs`
2. Click on "Authorize" button
3. Use the login endpoint with credentials:
   - Username: `admin`
   - Password: `admin123`
4. Copy the returned access token
5. Click "Authorize" again and paste the token in the format: `Bearer YOUR_TOKEN_HERE`
6. Now you can test all endpoints through the web interface

### Option 2: Using the Test Script

Run the comprehensive test script:

```bash
python test_api.py
```

This will test all endpoints and show you the expected request/response format.

### Option 3: Using curl commands

1. **Login and get token:**
   ```bash
   curl -X POST "http://localhost:8000/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=admin&password=admin123"
   ```

2. **Use the token for authenticated requests:**
   ```bash
   # Replace YOUR_TOKEN_HERE with the actual token
   curl -X GET "http://localhost:8000/employees" \
     -H "Authorization: Bearer YOUR_TOKEN_HERE"
   ```

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/token` | Login and get access token |
| POST | `/register` | Register new user |

### Employee Management

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/employees` | List all employees | ✅ |
| POST | `/employees` | Create new employee | ✅ |
| GET | `/employees/{id}` | Get employee by ID | ✅ |
| PUT | `/employees/{id}` | Update employee | ✅ |
| DELETE | `/employees/{id}` | Delete employee | ✅ |

### Task Management

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/tasks` | List all tasks | ✅ |
| POST | `/tasks` | Create new task | ✅ |
| GET | `/tasks/{id}` | Get task by ID | ✅ |
| PUT | `/tasks/{id}` | Update task | ✅ |
| DELETE | `/tasks/{id}` | Delete task | ✅ |

## Usage Examples

### 1. Login
```bash
curl -X POST "http://localhost:8000/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=admin123"
```

Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### 2. List Employees
```bash
curl -X GET "http://localhost:8000/employees" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

### 3. Create Employee
```bash
curl -X POST "http://localhost:8000/employees" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john.doe@company.com",
    "department": "Engineering",
    "position": "Software Developer"
  }'
```

### 4. Create Task
```bash
curl -X POST "http://localhost:8000/tasks" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Implement feature X",
    "description": "Add new authentication feature",
    "due_date": "2024-12-31T23:59:59",
    "employee_id": 1
  }'
```

### 5. Update Task Status
```bash
curl -X PUT "http://localhost:8000/tasks/1" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "status": "completed"
  }'
```

## Data Models

### Employee
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@company.com",
  "department": "Engineering",
  "position": "Software Developer",
  "created_at": "2024-01-01T10:00:00"
}
```

### Task
```json
{
  "id": 1,
  "title": "Implement feature X",
  "description": "Add new authentication feature",
  "status": "pending",  // pending, ongoing, completed
  "due_date": "2024-12-31T23:59:59",
  "employee_id": 1,
  "created_at": "2024-01-01T10:00:00",
  "updated_at": "2024-01-01T10:00:00",
  "employee": {
    "name": "John Doe",
    "email": "john.doe@company.com",
    "department": "Engineering",
    "position": "Software Developer"
  }
}
```

## Task Status Values
- `pending`: Task has not been started
- `ongoing`: Task is currently being worked on
- `completed`: Task has been finished

## Testing

### Automated Testing
Run the comprehensive test script:
```bash
python test_api.py
```

### Manual Testing
1. Visit `http://localhost:8000/docs` for interactive API documentation
2. Use the "Authorize" button to login with credentials:
   - Username: `admin`
   - Password: `admin123`
3. Test all endpoints through the Swagger UI

### Default Test Data
The database is seeded with:
- 1 user account (admin/admin123)
- 4 sample employees
- 5 sample tasks with different statuses

## Database Schema

### Tables
- `users`: Authentication credentials
- `employees`: Employee information
- `tasks`: Task details with employee assignments

### Relationships
- One-to-Many: Employee → Tasks
- Each task can be assigned to one employee
- Each employee can have multiple tasks

## Security Features

- **JWT Authentication**: Stateless authentication with expiring tokens
- **Password Hashing**: Secure bcrypt password storage
- **Input Validation**: Pydantic models validate all inputs
- **SQL Injection Protection**: SQLAlchemy ORM prevents SQL injection
- **Email Validation**: Proper email format validation

## Error Handling

The API returns appropriate HTTP status codes:
- `200`: Success
- `201`: Created
- `400`: Bad Request (validation errors)
- `401`: Unauthorized (authentication required)
- `404`: Not Found
- `422`: Unprocessable Entity (validation errors)

## 🛠 Technology Stack

### Backend
- **FastAPI** - Modern, fast web framework for building APIs
- **PostgreSQL** - Robust relational database
- **SQLAlchemy** - SQL toolkit and ORM
- **Pydantic** - Data validation and settings management
- **JWT (python-jose)** - JSON Web Token authentication
- **Passlib** - Password hashing utilities
- **Uvicorn** - ASGI web server implementation

### Frontend
- **React 19** - Modern React with latest features
- **TypeScript** - Static type checking for JavaScript
- **Material-UI (MUI)** - React components implementing Google's Material Design
- **React Router** - Declarative routing for React
- **Axios** - Promise-based HTTP client
- **Day.js** - Modern JavaScript date utility library
- **Vite** - Next generation frontend build tool
- **PNPM** - Fast, disk space efficient package manager

## 📁 Project Structure

```
employee-task-manager/
├── 📁 Backend (FastAPI)
│   ├── .env                    # Environment variables (create this)
│   ├── .gitignore             # Git ignore rules
│   ├── README.md              # Main project documentation
│   ├── requirements.txt       # Python dependencies
│   ├── main.py               # FastAPI application and routes
│   ├── models.py             # SQLAlchemy database models
│   ├── schemas.py            # Pydantic request/response schemas
│   ├── database.py           # Database configuration
│   ├── auth.py               # Authentication utilities
│   ├── init_db.py            # Database initialization script
│   ├── test_api.py           # API testing script
│   ├── setup.sh              # Automated setup script (Linux/macOS)
│   ├── setup.bat             # Automated setup script (Windows)
│   └── fastapi-env/          # Virtual environment (auto-created)
│
├── 📁 Frontend (React)
│   └── emp-task-mangr-client/
│       ├── public/           # Static assets
│       ├── src/
│       │   ├── components/   # Reusable UI components
│       │   │   ├── Layout.tsx
│       │   │   └── ProtectedRoute.tsx
│       │   ├── contexts/     # React contexts
│       │   │   └── AuthContext.tsx
│       │   ├── pages/        # Page components
│       │   │   ├── LoginPage.tsx
│       │   │   ├── EmployeePage.tsx
│       │   │   └── TaskPage.tsx
│       │   ├── services/     # API integration
│       │   │   └── api.ts
│       │   ├── App.tsx       # Main app component
│       │   └── main.tsx      # App entry point
│       ├── package.json      # Frontend dependencies
│       ├── vite.config.ts    # Vite configuration
│       ├── tsconfig.json     # TypeScript configuration
│       └── README.md         # Frontend documentation
│
└── 📄 Documentation
    └── PROJECT_SUMMARY.md     # Detailed project summary
```

## Sample Data

After running `python init_db.py`, the database will contain:

### Users
- **Admin User**: `admin` / `admin123`

### Employees
1. **John Doe** - Engineering, Software Developer
2. **Jane Smith** - Marketing, Marketing Manager
3. **Mike Johnson** - Engineering, Senior Developer
4. **Sarah Wilson** - HR, HR Specialist

### Tasks
1. **Implement user authentication** (ongoing) - Assigned to John Doe
2. **Design marketing campaign** (pending) - Assigned to Jane Smith
3. **Code review process setup** (completed) - Assigned to Mike Johnson
4. **Employee handbook update** (pending) - Assigned to Sarah Wilson
5. **Database optimization** (ongoing) - Assigned to John Doe

## License

This project is for educational/demonstration purposes.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#troubleshooting) section
2. Review the API documentation at `http://localhost:8000/docs`
3. Run the test script: `python test_api.py`

---

## ⚡ Quick Command Reference

### Backend Commands
```bash
# Setup Backend
python -m venv fastapi-env
source fastapi-env/bin/activate  # macOS/Linux
# fastapi-env\Scripts\activate   # Windows
pip install -r requirements.txt

# Database Setup
python init_db.py

# Run Backend Server
uvicorn main:app --reload --port 8000

# Test Backend API
python test_api.py

# Access Backend Documentation
# http://localhost:8000/docs
```

### Frontend Commands
```bash
# Setup Frontend
cd emp-task-mangr-client
npm install -g pnpm  # Install pnpm globally
pnpm install

# Run Frontend Development Server  
pnpm dev

# Build Frontend for Production
pnpm build

# Preview Production Build
pnpm preview

# Run Linting
pnpm lint

# Access Frontend Application
# http://localhost:5173
```

### Full Stack Development
```bash
# Terminal 1: Backend
source fastapi-env/bin/activate
uvicorn main:app --reload --port 8000

# Terminal 2: Frontend  
cd emp-task-mangr-client
pnpm dev

# Access:
# Frontend: http://localhost:5173
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

## 🔧 Development Workflow

### Starting Development

1. **Start Backend** (Terminal 1):
   ```bash
   source fastapi-env/bin/activate
   uvicorn main:app --reload --port 8000
   ```

2. **Start Frontend** (Terminal 2):
   ```bash
   cd emp-task-mangr-client
   pnpm dev
   ```

3. **Open Application**: http://localhost:5173

### Making Changes

- **Backend**: Edit Python files → Server auto-reloads
- **Frontend**: Edit React/TypeScript files → Browser auto-reloads
- **Database**: Modify models → Re-run `python init_db.py`

### Building for Production

1. **Build Frontend**:
   ```bash
   cd emp-task-mangr-client
   pnpm build
   ```

2. **Run Backend in Production**:
   ```bash
   gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
   ```

## 🚨 Troubleshooting

### Common Issues and Solutions

#### Backend Issues

##### 1. **PostgreSQL Connection Error**
```
sqlalchemy.exc.OperationalError: connection to server at "localhost"
```

**Solutions:**
- Ensure PostgreSQL is installed and running
- Check if the database `employee_db` exists
- Verify username/password in `.env` file
- Test connection: `psql -U postgres -d employee_db`

##### 2. **Python Module Errors**
```
ModuleNotFoundError: No module named 'fastapi'
```

**Solutions:**
- Ensure virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`
- Check Python version: `python --version` (should be 3.8+)

##### 3. **Port Already in Use**
```
OSError: [Errno 48] Address already in use
```

**Solutions:**
- Use a different port: `uvicorn main:app --port 8001`
- Kill existing process: `lsof -ti:8000 | xargs kill -9`

#### Frontend Issues

##### 1. **PNPM Not Found**
```
command not found: pnpm
```

**Solutions:**
```bash
# Install pnpm globally
npm install -g pnpm

# Or use npx
npx pnpm install
```

##### 2. **Node Version Issues**
```
error The engine "node" is incompatible with this module
```

**Solutions:**
- Install Node.js 16+ from https://nodejs.org/
- Use nvm to manage Node versions: `nvm install 16 && nvm use 16`

##### 3. **API Connection Error**
```
Network Error / CORS Error
```

**Solutions:**
- Ensure backend is running on http://localhost:8000
- Check CORS settings in FastAPI backend
- Verify API base URL in `src/services/api.ts`

##### 4. **Build Errors**
```
TypeScript compilation errors
```

**Solutions:**
- Run `pnpm install` to update dependencies
- Check for TypeScript errors: `pnpm build`
- Verify import paths and type definitions

#### Authentication Issues

##### 1. **Login Failed**
```
401 Unauthorized / Invalid credentials
```

**Solutions:**
- Verify credentials: `admin` / `admin123`
- Check if backend database is initialized: `python init_db.py`
- Clear browser localStorage and try again

##### 2. **Token Expired**
```
Token has expired
```

**Solutions:**
- Login again (tokens expire in 30 minutes by default)
- Check `ACCESS_TOKEN_EXPIRE_MINUTES` in `.env`

#### Database Issues

##### 1. **Table Does Not Exist**
```
ProgrammingError: relation "employees" does not exist
```

**Solutions:**
- Run database initialization: `python init_db.py`
- Check PostgreSQL connection
- Verify database name in `.env` file

##### 2. **Permission Denied**
```
permission denied for relation employees
```

**Solutions:**
- Check PostgreSQL user permissions
- Ensure database user has CREATE/READ/WRITE privileges
- Run as superuser: `CREATE DATABASE employee_db OWNER postgres;`

### Development Tips

#### Backend Development
```bash
# Start with detailed logging
uvicorn main:app --reload --log-level debug --port 8000

# Run with custom host for network access
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend Development
```bash
# Start with specific port
pnpm dev --port 3000

# Build and preview
pnpm build && pnpm preview

# Run with network access
pnpm dev --host 0.0.0.0
```

### Browser Support

#### Frontend Requirements
- **Chrome**: 80+
- **Firefox**: 75+
- **Safari**: 13+
- **Edge**: 80+

### Performance Optimization

#### Backend
- Use connection pooling for database
- Implement caching for frequently accessed data
- Add database indexes for better query performance

#### Frontend
- Use React.memo for expensive components
- Implement virtual scrolling for large lists
- Optimize bundle size with code splitting

---

**Happy Coding! 🚀**