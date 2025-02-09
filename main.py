from fastapi import FastAPI
from app.routes.health_routes import health_route
from app.routes.logs_routers import logs_router
PREFIX = "/api/v1/inventory/"
app = FastAPI(
    title="Inventory Manager API",
    version="1.1.0",
    description="API for managing inventory"
)
app = FastAPI()


# Health routes
app.include_router(health_route, prefix=f"{PREFIX}health", tags=["health"])

# Logs routes
app.include_router(logs_router, prefix=f"{PREFIX}logs", tags=["logs"])