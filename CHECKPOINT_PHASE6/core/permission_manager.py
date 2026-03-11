def request_permission(next_size):

    ans = input(
        f"Dataset expansion to {next_size} parameters. Approve? y/n:"
    )

    return ans.lower() == "y"
