def migrate_up(manager):
    manager.execute("ALTER TABLE tests MODIFY invalid TINYINT(1) DEFAULT 0")


def migrate_down(manager):
    manager.execute("ALTER TABLE tests MODIFY invalid TINYINT(1) DEFAULT NULL")
