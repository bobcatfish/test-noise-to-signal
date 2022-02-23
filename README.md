# Get a useful signal out of tests, minimize the noise

* [Manning Twitch stream Feb 23, 2022](https://www.twitch.tv/manningpublications/schedule?seriesID=7f6bd1c8-5c6e-4e74-8dac-6faa55730700)
* [Slides](https://docs.google.com/presentation/d/1TffyautuQJXdeEhgYKYYICgh6nhfBvvWosV9WPrgDwI)

Learn the difference between signal and noise when it comes to tests - it might not be what you expect!
We'll walk through some examples of noisy passing tests, and noisy flakey tests, and talk about why
retrying flakey tests will actually increase the noise in your tests.

## Outline

1. [Define signal versus noise](https://docs.google.com/presentation/d/1TffyautuQJXdeEhgYKYYICgh6nhfBvvWosV9WPrgDwI/edit#slide=id.g116f8da5611_0_1)
1. [Describe how to handle test noise](https://docs.google.com/presentation/d/1TffyautuQJXdeEhgYKYYICgh6nhfBvvWosV9WPrgDwI/edit#slide=id.g116f8da5611_0_44)
1. Show examples of passing tests:
    1. Test that passes (success + signal) `test_add_item_multiple`
    1. Test that passes but shouldn’t (success but should fail) `test_get_most_recent`
1. Fix the test that passes but shouldn't
1. Show examples of failing tests:
    1. Failure that provides new information `test_submit_orders` (logic broken), `test_get_total_orders` (test broken)
    1. Failure that doesn’t provide new information (tests that are left broken, flakes)
1. Fix the failing tests
1. [Describe flakey tests](https://docs.google.com/presentation/d/1TffyautuQJXdeEhgYKYYICgh6nhfBvvWosV9WPrgDwI/edit#slide=id.g116f8da5611_0_34)
1. Show example of a flakey test `test_process_order`
1. Fix the flakey test
    1. Using retry on the entire function `@retry.retry(retries=3)`
    1. Using retry on the connect function only `retry_network_errors(mrf.connect, retries=3)`
    1. Update the connect function itself to backoff and retry (using [backoff lib](https://pypi.org/project/backoff/))
1. If extra time: explore some real life flakey tests