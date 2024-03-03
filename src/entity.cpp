#include "entity.h"
#include "SQLiteCpp/Database.h"
#include "persister.h"
#include <iostream>


EntityRegistry::EntityRegistry(): db("./db/matrix.db",
                                     SQLite::OPEN_READWRITE | SQLite::OPEN_CREATE) {}

SQLite::Database &EntityRegistry::getDatabase() {
  return db;
}

void EntityRegistry::createTablesIfNeeded() {
  db.exec("CREATE TABLE IF NOT EXISTS Entity "
          "(id INTEGER PRIMARY KEY)");

  for(auto persister: persisters) {
    persister->createTablesIfNeeded();
  }
}

void EntityRegistry::saveAll() {
  for (auto persister : persisters) {
    persister->saveAll();
  }
}

void EntityRegistry::save(entt::entity e) {
  for (auto persister : persisters) {
    persister->save(e);
  }
}


void EntityRegistry::loadAll() {
  SQLite::Statement query(db, "SELECT * FROM Entity");
  while (query.executeStep()) {
    int entityId = query.getColumn(0).getInt();
    entt::entity newEntity = create();
    emplace<Persistable>(newEntity, entityId);
  }
  for (auto persister : persisters) {
    persister->loadAll();
  }
}

void EntityRegistry::load(entt::entity e) {
  // this is useless
  for (auto persister : persisters) {
    persister->load(e);
  }
}

void EntityRegistry::addPersister(std::shared_ptr<SQLPersister> p) {
  persisters.push_back(p);
}

entt::entity EntityRegistry::createPersistent() {
  SQLite::Statement query(db, "INSERT INTO Entity (id) VALUES (NULL)");
  query.exec();
  int64_t id = db.getLastInsertRowid();
  auto rv = this->create();
  emplace<Persistable>(rv, id);
  return rv;
}
