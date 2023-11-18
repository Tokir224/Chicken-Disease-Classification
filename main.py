from chicken_disease import logger
from chicken_disease.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from chicken_disease.pipeline.stage_02_prepare_base_model import (
    PrepareBaseModelTrainingPipeline,
)


STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data ingestion stage"

try:
    logger.info("*****************************************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===================x")
except Exception as e:
    logger.exception(e)
    raise e
