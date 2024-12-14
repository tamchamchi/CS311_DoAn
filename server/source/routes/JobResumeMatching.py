from fastapi import APIRouter, Request, Body
from source.models.candidate import Candidate
from source.models.job import JobDescription
from source.controller.JobResumeMatching import createJobResumeMatching, getTopKJobResumeMatching


router = APIRouter()

@router.post("/createJobResumeMatching")
async def create_job_resume_matching(request: Request, Candidate: Candidate = Body(...), JobDescription: JobDescription = Body(...)):
     return await createJobResumeMatching(request, Candidate, JobDescription)

@router.get("/getTopKJobResumeMatching/{k}")
async def get_top_k_job_resume_matching(request: Request, k: int):
     return await getTopKJobResumeMatching(request, k)