from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()
logger = get_logger(__name__)


def main():
    try:
        logger.info("Starting to build pipeline...")

        # Load and preprocess data
        loader = AnimeDataLoader(
            raw_csv_path="data/anime_with_synopsis.csv",
            processed_csv_path="data/anime_updated.csv"
        )
        processed_csv = loader.load_and_process()
        logger.info("Data loaded and processed successfully")

        # Build vector store
        vector_builder = VectorStoreBuilder(csv_path=processed_csv)
        vector_builder.build_and_save_vectorstore()
        logger.info("Vector store built successfully")

        logger.info("Pipeline built successfully")

    except Exception as e:
        logger.error(f"Failed to execute pipeline: {str(e)}")
        raise CustomException("Error during pipeline execution", e)


if __name__ == "__main__":
    main()
