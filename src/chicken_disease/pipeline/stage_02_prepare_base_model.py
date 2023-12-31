from chicken_disease import logger
from chicken_disease.components.prepare_base_model import PrepareBaseModel
from chicken_disease.config.configuration import ConfigurationManager


STAGE_NAME = "Prepare base model"


class PrepareBaseModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == "__main__":
    try:
        logger.info("*****************************************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(
            f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===================x"
        )
    except Exception as e:
        logger.exception(e)
        raise e
