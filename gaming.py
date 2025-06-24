import mysql.connector
from mysql.connector import Error

def connect_db():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="0805Fbpfk",
            database="GamingZone"
        )
    except Error as e:
        print("Connection error:", e)
        return None

def list_games():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Games")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def list_members():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Members")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def list_membership_by_type(mtype):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Members WHERE membership_type = %s", (mtype,))
    for row in cursor.fetchall():
        print(row)
    conn.close()

def member_hours_info():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name, membership_type, hours_left FROM Members")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def count_monthly_members():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Members WHERE membership_type = 'monthly'")
    print("Monthly members:", cursor.fetchone()[0])
    conn.close()

def game_player_count(game_name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT COUNT(DISTINCT gp.member_id)
        FROM Game_Play gp
        JOIN Games g ON gp.game_id = g.game_id
        WHERE g.game_name = %s
    """, (game_name,))
    print(f"Players who played {game_name}:", cursor.fetchone()[0])
    conn.close()

def total_game_hours(game_name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT SUM(gp.hours_played)
        FROM Game_Play gp
        JOIN Games g ON gp.game_id = g.game_id
        WHERE g.game_name = %s
    """, (game_name,))
    result = cursor.fetchone()[0]
    print(f"Total hours played for {game_name}:", result if result else 0)
    conn.close()

def most_played_game():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT g.game_name, SUM(gp.hours_played) AS total_hours
        FROM Game_Play gp
        JOIN Games g ON gp.game_id = g.game_id
        GROUP BY g.game_id
        ORDER BY total_hours DESC
        LIMIT 1
    """)
    result = cursor.fetchone()
    print("Most played game:", result[0], "| Hours:", result[1])
    conn.close()

def add_game(name, gtype, charge):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Games (game_name, game_type, charge_per_hour) VALUES (%s, %s, %s)", (name, gtype, charge))
    conn.commit()
    print("Game added successfully.")
    conn.close()

def register_member(name, mtype):
    hours = {"daily": 3, "monthly": 20, "yearly": 100}
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Members (name, membership_type, hours_spent, hours_left) VALUES (%s, %s, %s, %s)", (name, mtype, 0, hours[mtype]))
    conn.commit()
    print("Member registered successfully.")
    conn.close()

def log_gameplay(member_name, game_name, hours):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT member_id, hours_left FROM Members WHERE name = %s", (member_name,))
    member = cursor.fetchone()
    if not member:
        print("Member not found.")
        conn.close()
        return
    member_id, hours_left = member

    cursor.execute("SELECT game_id FROM Games WHERE game_name = %s", (game_name,))
    game = cursor.fetchone()
    if not game:
        print("Game not found.")
        conn.close()
        return
    game_id = game[0]

    if hours_left < hours:
        print("Not enough hours left.")
        conn.close()
        return

    cursor.execute("INSERT INTO Game_Play (member_id, game_id, hours_played, play_date) VALUES (%s, %s, %s, NOW())", (member_id, game_id, hours))
    cursor.execute("UPDATE Members SET hours_spent = hours_spent + %s, hours_left = hours_left - %s WHERE member_id = %s", (hours, hours, member_id))
    conn.commit()
    print("Gameplay logged.")
    conn.close()

def delete_inactive_members():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM Members
        WHERE member_id NOT IN (SELECT DISTINCT member_id FROM Game_Play)
    """)
    conn.commit()
    print("Inactive members deleted.")
    conn.close()

def view_expensive_games():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Games WHERE charge_per_hour > 100")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def count_games_by_type():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT game_type, COUNT(*) FROM Games GROUP BY game_type")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def members_below_10():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Members WHERE hours_left < 10")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def members_played_more_than_2():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT member_id
        FROM Game_Play
        GROUP BY member_id
        HAVING COUNT(DISTINCT game_id) > 2
    """)
    for row in cursor.fetchall():
        print("Member ID:", row[0])
    conn.close()

def total_hours_remaining():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT membership_type, SUM(hours_left) FROM Members GROUP BY membership_type")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def total_income():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT SUM(g.charge_per_hour * gp.hours_played)
        FROM Game_Play gp
        JOIN Games g ON gp.game_id = g.game_id
    """)
    result = cursor.fetchone()[0]
    print("Total income: ₹", result)
    conn.close()

def most_active_member():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM Members ORDER BY hours_spent DESC LIMIT 1")
    print("Most active member:", cursor.fetchone()[0])
    conn.close()

def top_3_games():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT g.game_name, SUM(gp.hours_played) AS total
        FROM Game_Play gp
        JOIN Games g ON gp.game_id = g.game_id
        GROUP BY g.game_id
        ORDER BY total DESC
        LIMIT 3
    """)
    for row in cursor.fetchall():
        print(row)
    conn.close()

def member_game_report():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.name, g.game_name, SUM(gp.hours_played)
        FROM Game_Play gp
        JOIN Members m ON gp.member_id = m.member_id
        JOIN Games g ON gp.game_id = g.game_id
        GROUP BY m.name, g.game_name
    """)
    for row in cursor.fetchall():
        print(row)
    conn.close()

def heavy_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM Members WHERE hours_spent / (hours_spent + hours_left) > 0.75")
    for row in cursor.fetchall():
        print("Heavy user:", row[0])
    conn.close()

def detailed_report():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.name, m.membership_type,
        COUNT(DISTINCT gp.game_id) AS games_played,
        SUM(gp.hours_played) AS total_hours,
        m.hours_left
        FROM Members m
        LEFT JOIN Game_Play gp ON m.member_id = gp.member_id
        GROUP BY m.member_id
    """)
    for row in cursor.fetchall():
        print(row)
    conn.close()

def never_played():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name FROM Members
        WHERE member_id NOT IN (SELECT DISTINCT member_id FROM Game_Play)
    """)
    for row in cursor.fetchall():
        print("Never played:", row[0])
    conn.close()

# MENU SYSTEM
def menu():
    while True:
        print("\n--- Gaming Zone Menu ---")
        print("1. List Games")
        print("2. List Members")
        print("3. List Members by Type")
        print("4. Show Member Info")
        print("5. Count Monthly Members")
        print("6. Game Player Count")
        print("7. Total Game Hours")
        print("8. Most Played Game")
        print("9. Add Game")
        print("10. Register Member")
        print("11. Log Gameplay")
        print("12. Delete Inactive Members")
        print("13. View Expensive Games")
        print("14. Count Games by Type")
        print("15. Members with <10 Hours")
        print("16. Members Played >2 Games")
        print("17. Hours Remaining by Membership Type")
        print("18. Total Income")
        print("19. Most Active Member")
        print("20. Top 3 Played Games")
        print("21. Member-Game Hours")
        print("22. Heavy Users (>75%)")
        print("23. Detailed Member Report")
        print("24. Never Played Members")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1': list_games()
        elif choice == '2': list_members()
        elif choice == '3':
            t = input("Enter type (daily/monthly/yearly): ")
            list_membership_by_type(t)
        elif choice == '4': member_hours_info()
        elif choice == '5': count_monthly_members()
        elif choice == '6':
            name = input("Enter game name: ")
            game_player_count(name)
        elif choice == '7':
            name = input("Enter game name: ")
            total_game_hours(name)
        elif choice == '8': most_played_game()
        elif choice == '9':
            name = input("Game name: ")
            gtype = input("Game type: ")
            charge = int(input("Charge per hour: "))
            add_game(name, gtype, charge)
        elif choice == '10':
            name = input("Member name: ")
            mtype = input("Membership type: ")
            register_member(name, mtype)
        elif choice == '11':
            name = input("Member name: ")
            gname = input("Game name: ")
            hrs = int(input("Hours to play: "))
            log_gameplay(name, gname, hrs)
        elif choice == '12': delete_inactive_members()
        elif choice == '13': view_expensive_games()
        elif choice == '14': count_games_by_type()
        elif choice == '15': members_below_10()
        elif choice == '16': members_played_more_than_2()
        elif choice == '17': total_hours_remaining()
        elif choice == '18': total_income()
        elif choice == '19': most_active_member()
        elif choice == '20': top_3_games()
        elif choice == '21': member_game_report()
        elif choice == '22': heavy_users()
        elif choice == '23': detailed_report()
        elif choice == '24': never_played()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()
