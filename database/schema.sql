CREATE TABLE IF NOT EXISTS "games" (
	"id"	INTEGER NOT NULL UNIQUE,
	"game_name"	TEXT NOT NULL,
	"start_timestamp"	NUMERIC NOT NULL,
	"interval"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
)