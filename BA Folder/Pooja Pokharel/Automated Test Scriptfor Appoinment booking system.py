from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver
driver = webdriver.Chrome()  # You may need to specify the path to your WebDriver executable

# Navigate to the Appointment Booking System login page
driver.get("https://example.com/login")  # Replace with the actual URL

# Maximize the window
driver.maximize_window()

try:
    # Login Test Case
    print("Starting Login Test Case...")
    
    # Locate and fill in the username field
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys("testuser")  # Replace with test username

    # Locate and fill in the password field
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("password123")  # Replace with test password

    # Submit the login form
    password_field.send_keys(Keys.RETURN)

    # Wait for the dashboard page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dashboard")))
    print("Login Test Case Passed!")

    # Appointment Booking Test Case
    print("Starting Appointment Booking Test Case...")

    # Navigate to the appointment booking page
    driver.find_element(By.LINK_TEXT, "Book Appointment").click()

    # Wait for the appointment booking form to appear
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "appointment-form")))

    # Select a doctor from the dropdown
    doctor_dropdown = driver.find_element(By.NAME, "doctor")
    doctor_dropdown.click()
    doctor_option = driver.find_element(By.XPATH, "//option[text()='Dr. John Doe']")
    doctor_option.click()

    # Select a date for the appointment
    date_field = driver.find_element(By.NAME, "date")
    date_field.send_keys("12/10/2024")  # Use the desired date format

    # Select a time slot
    time_field = driver.find_element(By.NAME, "time")
    time_field.send_keys("10:00 AM")  # Use the desired time

    # Submit the appointment form
    submit_button = driver.find_element(By.XPATH, "//button[text()='Confirm Appointment']")
    submit_button.click()

    # Wait for the confirmation message
    confirmation_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "confirmation-message"))
    )
    print("Appointment Booking Test Case Passed!")

except Exception as e:
    print("Test Case Failed:", e)

finally:
    # Close the WebDriver
    time.sleep(3)
    driver.quit()
