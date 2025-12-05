# Automation Portofolio : Pytest API Testing - AirportGap
A comprehensive API test automation framework for the [AirportGap](https://airportgap.com/) using Pytest and the Requests library with Python.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running Tests](#running-tests)
- [Test Coverage](#test-coverage)
- [API Endpoints Tested](#api-endpoints-tested)
- [Author](#author)

## Overview
This project demonstrates API testing practices using the AirportGap public API. The framework follows the Page Object Model pattern adapted for API testing, ensuring maintainable and scalable test code. It includes comprehensive test coverage for positive scenarios, negative scenarios, and end-to-end workflows.
<div align="right"><a href="#table-of-contents">Back to Top</a></div>


## Features
<li>Page Object Model for APIs: clean separation of API endpoints and test logic</li>
<li>Comprehensive Test Coverage: positive, negative, and E2E test scenarios</li>
<li>Authentication Handling: token-based authentication with session management</li>
<li>Parameterized Testing: data-driven tests using pytest parametrize</li>
<li>Reusable Fixtures: pre-configured sessions and authenticated clients</li>
<li>RESTful API Testing: GET, POST, PATCH, DELETE methods</li>
<li>Response Validation: status codes, response structure, and data validation</li>
<li>Session Management: persistent session handling with requests library</li>
<div align="right"><a href="#table-of-contents">Back to Top</a></div>



## Project Structure
<pre>
Pytest-API/
├── tests/
│   ├── pages/
│   │   ├── airport_page.py          # Airport API endpoints wrapper
│   │   └── auth.py                  # Authentication client
│   ├── test_api/
│   │   ├── test_airportgap_positive.py    # Positive test scenarios
│   │   ├── test_airportgap_negative.py    # Negative test scenarios
│   │   └── test_airportgap_e2e.py         # End-to-end workflows
│   ├── __init__.py
│   └── conftest.py                  # Pytest fixtures and configuration
├── .gitignore
└── README.md
</pre>
<div align="right"><a href="#table-of-contents">Back to Top</a></div>


## Prerequisites
<h4>Before running this project, ensure you have the following installed:</h4>

<li> Python 3.8+ </li>
<li> pip (Python package manager) </li>
<li> Git </li>
<div align="right"><a href="#table-of-contents">Back to Top</a></div>


## Installation
<h3>1. Clone the repository</h3>
<pre>bash<br>
git clone https://github.com/saisyah101/Pytest-API.git 
cd Pytest-API </pre>

<h3>2. Create and activate virtual environment</h3>
<pre>bash<br>
# Windows
python -m venv venv
venv\Scripts\activate
<br>
# macOS/Linux
python3 -m venv venv 
source venv/bin/activate</pre>

<h3>3. Install dependencies</h3>
<pre>bash<br>
pip install pytest 
pip install requests 
pip install pytest-html</pre>
<div align="right"><a href="#table-of-contents">Back to Top</a></div>

                         


## Running Tests
<h3>Run all tests</h3>
<pre>bash<br>
pytest</pre>


<h3>Run specific test</h3>
<pre>bash<br>
# Positive tests only
pytest tests/test_api/test_airportgap_positive.py<br>
# # Negative tests only 
pytest tests/test_api/test_airportgap_negative.py<br>
# End-to-end tests only 
pytest tests/test_api/test_airportgap_e2e.py</pre>

<h3>Run tests with verbose output</h3>
<pre>bash<br>
pytest -v</pre>

<h3>Run tests in parallel (faster execution)</h3>
<pre>bash<br>
pip install pytest-xdist 
pytest -n auto</pre>

<h3>Run tests with HTML report</h3>
<pre>bash<br>
pytest --html=report.html --self-contained-html</pre>

<h3>Run specific test by name</h3>
<pre>bash<br>
pytest -k "test_get_airports_success"</pre>
<div align="right"><a href="#table-of-contents">Back to Top</a></div>


## Test Coverage
<h3>Positive Test Scenarios</h3>
<h3>Airport Endpoints (test_airportgap_positive.py)</h3>
<li>Get all airports successfully</li>
<li>Get airports with valid pagination (pages 2, 20, 200, 203)</li>
<li>Get airports with pagination returning no data (pages 205, 300, 500)</li>
<li>Get airport by ID (NRT, SWQ, CGK, DOH, GRX)</li>
<li>Calculate distance between airports</li>
<li>Calculate distance for same airport (zero distance)</li>

<h3>Favorites Endpoints (requires authentication)</h3>
<li>Get all favorites</li>
<li>Get favorite by ID</li>

<h3>Negative Test Scenarios</h3>
<h3>Airport Endpoints (test_airportgap_negative.py)</h3>
<li>Invalid pagination (page 0, -1)</li>
<li>Invalid distance calculation parameters</li>
<li>Unauthorized access to favorites</li>
<li>Invalid authentication credentials</li>
<li>Duplicate favorite airport</li>
<li>Delete non-existent favorite</li>

<h3>End-to-End Workflows</h3>
<h3>Favorites Management (test_airportgap_e2e.py)</h3>
<li>Complete workflow: Add favorite → Verify → Delete → Verify </li>
<li>Create favorite without note → Patch with note → Delete</li>
<li>Full CRUD operations on favorites</li>

<div align="right"><a href="#table-of-contents">Back to Top</a></div>

## API Endpoints Tested
<h3>Base URL</h3>
<pre>https://airportgap.com/api</pre>

<h3>Endpoints</h3>
<table>
  <thead>
    <tr>
      <th align="center">Method</th>
      <th>Endpoint</th>
      <th>Description</th>
      <th align="center">Auth Required</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><strong>GET</strong></td>
      <td>/airports</code></td>
      <td>Get all airports with pagination</td>
      <td align="center">NO</td>
    </tr>
    <tr>
      <td align="center"><strong>GET</strong></td>
      <td>/airports/{id}</code></td>
      <td>Get specific airport by ID</td>
      <td align="center">NO</td>
    </tr>
    <tr>
      <td align="center"><strong>POST</strong></td>
      <td>/airports/distance</code></td>
      <td>Calculate distance between airports</td>
      <td align="center">NO</td>
    </tr>
    <tr>
      <td align="center"><strong>GET</strong></td>
      <td>/favorites</code></td>
      <td>Get user's favorite airports</td>
      <td align="center">YES</td>
    </tr>
    <tr>
      <td align="center"><strong>GET</strong></td>
      <td>/favorites/{id}</code></td>
      <td>Get specific favorite by ID</td>
      <td align="center">YES</td>
    </tr>
    <tr>
      <td align="center"><strong>POST</strong></td>
      <td>/favorites</code></td>
      <td>Add airport to favorites</td>
      <td align="center">YES</td>
    </tr>
    <tr>
      <td align="center"><strong>PATCH</strong></td>
      <td>/favorites/{id}</code></td>
      <td>Update favorite note</td>
      <td align="center">YES</td>
    </tr>
    <tr>
      <td align="center"><strong>DELETE</strong></td>
      <td>/favorites/{id}</code></td>
      <td>Remove favorite airport</td>
      <td align="center">YES</td>
    </tr>
    <tr>
      <td align="center"><strong>POST</strong></td>
      <td>/tokens</code></td>
      <td>Authenticate and get token</td>
      <td align="center">NO</td>
    </tr>
  </tbody>
</table>
<div align="right"><a href="#table-of-contents">Back to Top</a></div>

## Author
Siti Aisyah<br>
[LinkedIn](https://www.linkedin.com/in/saisyah)
<div align="right"><a href="#table-of-contents">Back to Top</a></div>







