import mysql.connector
import os
from digital_hunter_map import plot_map_with_geometry

class SqlQueries:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = os.getenv('DB_HOST', 'localhost'),
            port = os.getenv('DB_PORT', 3307),
            database = os.getenv('DB_NAME', 'digital_hunter'),
            user = os.getenv('DB_USER', 'root'),
            password = os.getenv('DB_PASSWORD', 'root')
        )

    def shifting_quality_targets(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT entity_id, target_name, priority_level, movement_distance_km FROM targets WHERE (priority_level = 1 or priority_level = 2) and movement_distance_km > 5"
        )
        result = cursor.fetchall()
        return result

    def analysis_of_collection_sources(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT signal_type, COUNT(*) AS count FROM intel_signals GROUP BY signal_type ORDER BY count DESC"
        )
        result = cursor.fetchall()
        return result

    def finding_new_targets(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT entity_id, COUNT(*) AS count FROM intel_signals WHERE priority_level = 99 GROUP BY entity_id ORDER BY count DESC LIMIT 3"
        )
        result = cursor.fetchall()
        return result

    def identifying_targets_that_have_arisen(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT entity_id, distance_from_last FROM intel_signals WHERE distance_from_last >= 10"
        )
        result = cursor.fetchall()
        return result

    def visualization_of_target_trajectory(self, entity_id):
        cursor = self.conn.cursor()
        cursor.execute(
            f"SELECT reported_lon, reported_lat FROM intel_signals WHERE entity_id = '{entity_id}'"
        )
        points = cursor.fetchall()
        return plot_map_with_geometry(points, shapefile_path="ne_50m_admin_0_countries.shp")

    def analysis_of_escape_patterns_after_an_attack(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(
            ""
        )
        result = cursor.fetchall()
        return result

    def finding_meetings_between_quality_goals_and_unknown_entities(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(
            ""
        )
        result = cursor.fetchall()
        return result

if __name__ == '__main__':
    conn = SqlQueries()
    conn.visualization_of_target_trajectory('TGT-008')


