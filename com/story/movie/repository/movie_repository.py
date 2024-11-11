from com.story.config.logger_config import get_logger
from com.story.config.profile import active_profile
from com.story.movie.entity.movie_entity import movie_entity

logger = get_logger()
profile = active_profile()


class movie_repository:
    def save(self, wallet_block_transaction: movie_entity, session):
        session.add(wallet_block_transaction)
        logger.info(f"Saved wallet block transaction to database")

    def save_all(self, wallet_block_transaction_list: list[movie_entity], session):
        # Session = sessionmaker(bind=get_database_connection_exchange())
        # session = Session()
        session.bulk_save_objects(wallet_block_transaction_list)
        # logger.info(f"Saved {wallet_block_transaction_list.count} wallet block transaction to database")
