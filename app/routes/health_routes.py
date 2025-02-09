from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.config.logs_config import logger
from app.mongo.mongo_connection import check_connection
from app.postgres.postgres_connection import postgres_db




health_route = APIRouter()

@health_route.get(
    path="/",
    status_code=status.HTTP_200_OK,
    operation_id="Health_fastAPIHealth"
)
async def fast_api_health():
    try:
        logger.info("Testing FastAPI functionality")
        return JSONResponse(
            content={
                "success":True,
                "detal":"FastAPI funcionando correctamente."
            },
        )
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return JSONResponse(
            content={
                "success":False,
                "detail":f"Error: {str(e)}",
            },
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR 
        )

@health_route.get(
    path="/mongo_health/",
    status_code=status.HTTP_200_OK,
    operation_id="Health_mongoHealth"
)
async def mongo_health():
    try:
        logger.info("Testing MongoDB functionality")
        if not await check_connection():
            return JSONResponse(
                content={
                    "success": False,
                    "detail": "Falló la conexión a la base de datos"
                },
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE
            )
        return JSONResponse(
            content={
                "success": True,
                "detail": "Conexión a la base de datos exitosa"
            },
            status_code=status.HTTP_200_OK
        )
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return JSONResponse(
            content={
                "success":False,
                "detail":f"Error: {str(e)}",
            },
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR 
        )

@health_route.get(
    path="/postgresql_health/",
    status_code=status.HTTP_200_OK,
    operation_id="Health_postgresHealth"
)
async def postgresql_health():
    try:
        logger.info("Testing PostgreSQL functionality")
        if not postgres_db.pool:
            return JSONResponse(
                content={
                    "success": False,
                    "detail": "Falló la conexión a la base de datos"
                },
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE
            )
        return JSONResponse(
            content={
                "success": True,
                "detail": "Conexión a la base de datos exitosa"
            },
            status_code=status.HTTP_200_OK
        )
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return JSONResponse(
            content={
                "success":False,
                "detail":f"Error: {str(e)}",
            },
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR 
        )

        

        

        

        
