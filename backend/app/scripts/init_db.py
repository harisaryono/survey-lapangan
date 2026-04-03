from app.core.database import Base, engine
from app.models import Survey, SurveyForm, SurveyMember, User
from app.models.form_finding import FormFinding


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Database tables created.")
