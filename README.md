How to Use This Object Relations Code Challenge
1. Setup the Environment
Make sure Python 3.x is installed on your system. Open your terminal and navigate to the project root directory.

2. Initialize the Database
Create the SQLite database and necessary tables by running:

python scripts/setup_db.py

3. Seed the Database
Populate the database with initial sample data using the seeding script:

python -m lib.db.seed

You should see a confirmation message:

✅ Database seeded using model methods.

4. Run Custom Queries
Explore the models and relationships by running example queries with:

python -m scripts.run_queries

5. Debug and Explore
For interactive debugging and testing of model methods, run:

python -m lib.debug

6. Run Automated Tests
Verify that everything works as expected by running the test suite:

pytest
