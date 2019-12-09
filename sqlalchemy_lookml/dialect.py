from sqlalchemy.engine.default import DefaultDialect


class LookMLDialect(DefaultDialect):
    name = "lookml"
