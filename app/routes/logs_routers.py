from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse
import os
from app.config.logs_config import logger


logs_router = APIRouter()

@logs_router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    operation_id="Logs_getLog"
)
async def get_log():
    try:

        with open(os.path.join(os.getcwd(),"logs", "app.log"), "r") as log_file:
            logs = log_file.readlines()
        return JSONResponse(
            content={
            "success": True,
            "detail": "Logs obtenidos correctamente",
            "data": logs
            },
            status_code=status.HTTP_200_OK
        )
    except Exception as e:
        logger.error(f"Ocurrió un error al obtener los logs {str(e)}")
        return JSONResponse(
            content={
                "success":False,
                "detail":"Ocurrió un error al obtener los logs",
                "data":[]
            },
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@logs_router.get(
    path="/download/",
    status_code=status.HTTP_200_OK,
    operation_id="Logs_DownloadLog"
)
async def download_log():
    try:
        logger.info("Dowloading log file")

        return FileResponse(
            path=os.path.join(os.getcwd(), "logs", "app.log"),
            filename="app.log",
            media_type="application/octet-stream"
        )
    except Exception as e:
        logger(f"Error: {str(e)}")
        return JSONResponse(
            content={
                "success":False,
                "detail":f"Error {str(e)}"
            },
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@logs_router.delete(
    path="/",
    status_code=status.HTTP_200_OK,
    operation_id="Logs_DeleteLogs"
)
async def delete_log():
    try:
        logger.info("Deleting log file")

        with open(os.path.join(os.getcwd(),"logs", "app.log"), "w") as log_file:
            log_file.truncate(0)
            return JSONResponse(
                content={
                "success": True,
                "detail": "Logs eliminados correctamente"
                },
                status_code=status.HTTP_200_OK
            )

        return 
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return JSONResponse(
            content={
                "success":False,
                "detail": f"Error {str(e)}"
            },
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
