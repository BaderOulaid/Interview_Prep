
# meetings = [(0,1), (3,5), (4,8), (10,12), (9,10)]

# meetings = [(0,3), (1,4), (4,7), (7,10)]

# meetings = [(1,2),(2,3)]

meetings = [(1,10),(2,6),(10,13)]
def merge_meetings(meetings):
    sorted_meetings = sorted(meetings)
    merged_meetings = [sorted_meetings[0]]

    for meeting_start, meeting_end in sorted_meetings[1:]:
        last_merged_start, last_merged_end = merged_meetings[-1]

        if (meeting_start <= last_merged_end):
            merged_meetings[-1] = (last_merged_start, max(meeting_end, last_merged_end))
        else:
            merged_meetings.append((meeting_start,meeting_end))

    print merged_meetings



if __name__ == "__main__":
    merge_meetings(meetings)



# o(n) space
# o(n) * o(nlgn) -> o(nlgn)
