import mysql.connector

class SqlQueries:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            port = 3307,
            database='digital_hunter',
            user='root',
            password='root')

    def find_all(self, table_name):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(
            f"SELECT * FROM {table_name}"
        )
        result = cursor.fetchall()
        print(f'{table_name}:')
        for x in result:
            print(x)
        cursor.close()
        # self.conn.close()

    def shifting_quality_targets(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT entity_id, target_name, priority_level, movement_distance_km FROM targets WHERE priority_level = 1 or priority_level = 2 and movement_distance_km > 5"
        )
        result = cursor.fetchall()
        for x in result:
            print(x)
        cursor.close()

    def analysis_of_collection_sources(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT signal_type, COUNT(*) AS count FROM intel_signals GROUP BY signal_type ORDER BY count DESC"
        )
        result = cursor.fetchall()
        for x in result:
            print(x)
        cursor.close()
    # WHERE priority_level = 99
    def finding_new_targets(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT entity_id, COUNT(*) AS count FROM intel_signals WHERE priority_level = 99 GROUP BY entity_id ORDER BY count DESC LIMIT 3"
        )
        result = cursor.fetchall()
        for x in result:
            print(x)
        cursor.close()

    def identifying_targets_that_have_arisen(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(
            ""
        )
        result = cursor.fetchall()
        for x in result:
            print(x)
        cursor.close()

    def visualization_of_target_trajectory(self):
        pass

    def analysis_of_escape_patterns_after_an_attack(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(
            ""
        )
        result = cursor.fetchall()
        for x in result:
            print(x)
        cursor.close()

    def finding_meetings_between_quality_goals_and_unknown_entities(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(
            ""
        )
        result = cursor.fetchall()
        for x in result:
            print(x)
        cursor.close()

if __name__ == '__main__':
    conn = SqlQueries()

    # conn.find_all(table_name='attacks')
    # conn.find_all(table_name='damage_assessments')
    # conn.find_all(table_name='intel_signals')
    # conn.find_all(table_name='targets')

    # conn.shifting_quality_targets()
    # conn.analysis_of_collection_sources()
    conn.finding_new_targets()

