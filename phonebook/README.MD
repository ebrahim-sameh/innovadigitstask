# InnovaDigits simple phonebook Application


## Prerequisites

- **Docker:** Make sure you have Docker installed. You can download it from the [official Docker website](https://www.docker.com/get-started).

## Getting Started

1. **Clone the Repository:**

   ```
   git clone https://github.com/ebrahim-sameh/innovadigitstask
   cd innovadigitstask
   ```

2. **Build the Docker Image:**

   ```
   docker build -t mydjangoapp .
   ```

   This command builds the Docker image and tags it with the name `mydjangoapp`.

3. **Run the Docker Container:**

   ```
   docker run -p 8000:8000 mydjangoapp
   ```

   The `-p 8000:8000` flag maps port 8000 from your local machine to port 8000 inside the container. Adjust the ports if your Django application uses a different port.

4. **Access the Application:**

   Open your web browser and visit `http://localhost:8000/contacts` to access the Django application.

5. **View Logs (Optional):**

   If you want to view the logs of your running Docker container, use the following command in a new terminal window:

   ```
   docker ps
   ```

   Note the container ID or name of your running container, and then run:

   ```
   docker logs <container_id_or_name>
   ```

   Replace `<container_id_or_name>` with the actual ID or name of your running Docker container.

## Stopping the Application

To stop the application, press `Ctrl + C` in the terminal where the Docker container is running.

---

### Database Schema

The application has two models: `Contact` and `PhoneNumber`.

#### Contact Model
- **name** *(CharField)*: The name of the contact (max length: 100 characters).

#### PhoneNumber Model
- **contact** *(ForeignKey)*: A foreign key relationship to the `Contact` model, establishing a many-to-one relationship between contacts and phone numbers. When a contact is deleted, all associated phone numbers are deleted as well.
- **number** *(CharField)*: The phone number (max length: 20 characters).

### Relationships
- Each `PhoneNumber` is associated with a single `Contact`.
- Each `Contact` can have multiple `PhoneNumber` entries.
