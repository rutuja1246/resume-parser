import psycopg2
from config import DB_CONFIG


def get_connection():
    """
    Creates and returns a PostgreSQL connection.
    """

    try:
        connection = psycopg2.connect(**DB_CONFIG)

        print("✅ Connected to PostgreSQL!")

        return connection

    except Exception as e:
        print("Database Connection Error:")
        print(e)

        return None
    
def save_candidate(candidate):

        connection = get_connection()

        if connection is None:
            return

        cursor = connection.cursor()

        query = """
        INSERT INTO candidates
        (name, email, phone, degree, institution, field, skills)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (email)
        DO NOTHING;
        """

        education = candidate["education"]

        skills = ", ".join(candidate["skills"])

        values = (
            candidate["name"],
            candidate["email"],
            candidate["phone"],
            education["degree"],
            education["institution"],
            education["field"],
            skills
        )

        cursor.execute(query, values)

        connection.commit()

        cursor.close()
        connection.close()

        print("✅ Candidate saved successfully!")

def get_all_candidates():
    """
    Fetches all candidates from the database.
    """

    connection = get_connection()

    if connection is None:
        return []

    cursor = connection.cursor()

    query = """
    SELECT id, name, degree, email, phone, skills
    FROM candidates
    ORDER BY id;
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    candidates = []

    for row in rows:

        candidate = {
            "id":row[0],
            "name": row[1],
            "degree": row[2],
            "email": row[3],
            "phone": row[4],
            "skills": row[5]
        }

        candidates.append(candidate)

    cursor.close()
    connection.close()

    return candidates

def search_candidates(search_text):

    connection = get_connection()

    if connection is None:
        return []

    cursor = connection.cursor()

    query = """
    SELECT id, name, degree, email, phone, skills
    FROM candidates
    WHERE
        LOWER(name) LIKE LOWER(%s)
        OR LOWER(degree) LIKE LOWER(%s)
        OR LOWER(skills) LIKE LOWER(%s)
    ORDER BY id;
    """

    keyword = f"%{search_text}%"

    cursor.execute(
        query,
        (keyword, keyword, keyword)
    )

    rows = cursor.fetchall()

    candidates = []

    for row in rows:

        candidates.append({
            "id":row[0],
            "name": row[1],
            "degree": row[2],
            "email": row[3],
            "phone": row[4],
            "skills": row[5]
        })

    cursor.close()
    connection.close()

    return candidates

def get_candidate(id):

    connection = get_connection()

    if connection is None:
        return None

    cursor = connection.cursor()

    query = """
    SELECT *
    FROM candidates
    WHERE id = %s;
    """

    cursor.execute(query, (id,))

    row = cursor.fetchone()

    cursor.close()
    connection.close()

    if row is None:
        return None

    candidate = {

        "id": row[0],

        "name": row[1],

        "email": row[2],

        "phone": row[3],

        "degree": row[4],

        "institution": row[5],

        "field": row[6],

        "skills": row[7]

    }

    return candidate

def delete_candidate(id):

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    query = """
    DELETE FROM candidates
    WHERE id = %s;
    """

    cursor.execute(query, (id,))

    connection.commit()

    cursor.close()
    connection.close()

    print("✅ Candidate deleted successfully!")
    
if __name__ == "__main__":

    conn = get_connection()

    if conn:
        conn.close()
        print("Connection Closed.")