from instapy import InstaPy
from instapy.util import smart_run

import time
import patch
import reporter

patch.apply()
reporter.set_version("like-ff-2.1-try")  # set a version tag

SLEEP_BETWEEN_EACH_LIKE = 20

session = InstaPy(
    bypass_suspicious_attempt=True,
    headless_browser=True,
    use_firefox=True,
    **reporter.Arguments().all()
)

with smart_run(session):
    while True:
        cur = time.time()
        try:
            time.sleep(SLEEP_BETWEEN_EACH_LIKE)
            session.like_by_tags(['love'], amount=1, interact=False)

            time.sleep(SLEEP_BETWEEN_EACH_LIKE)
            session.like_by_tags(['instagood'], amount=1, interact=False)

            time.sleep(SLEEP_BETWEEN_EACH_LIKE)
            session.like_by_tags(['photooftheday'], amount=1, interact=False)

            time.sleep(SLEEP_BETWEEN_EACH_LIKE)
            session.like_by_tags(['fashion'], amount=1, interact=False)
            logger.warning( time.time() - cur)
        except Exception as e:
            reporter.error(e)
