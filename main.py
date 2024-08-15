from crewai import Crew, Process
from agents import social_media_content_creator, social_media_researcher, tag_developer
from tasks import scrape_article, write_blurb, tag_writer
from tools import url


crew = Crew(
    agents=[social_media_researcher, social_media_content_creator, tag_developer],
    tasks=[scrape_article, write_blurb, tag_writer],
    process=Process.sequential,  # Optional: Sequential task execution is default
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True,
)

result = crew.kickoff(inputs={"url": url})
print(result)
