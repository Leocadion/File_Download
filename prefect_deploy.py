from prefect import flow

# Source for the code to deploy (here, a GitHub repo)
SOURCE_REPO="https://github.com/prefecthq/demos.git"

if __name__ == "__main__":
    flow.from_source(
        source=SOURCE_REPO,
        entrypoint="my_gh_workflow.py:repo_info", # Specific flow to run
    ).deploy(
        name="my-first-deployment",
        work_pool_name="test_work_pool", # Work pool target
        cron="* * * * *", # Cron schedule (every minute)
    )