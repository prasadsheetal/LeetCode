class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0

        self.history=[[[0,0]]for _ in range(length)]

        

    def set(self, index: int, val: int) -> None:

        changes = self.history[index]

        if changes[-1][0] == self.snap_id:
            changes [-1][1] = val

        else:
            changes.append([self.snap_id,val])

        

    def snap(self) -> int:
        
        current_snap = self.snap_id
        self.snap_id += 1
        return current_snap

    def get(self, index: int, snap_id: int) -> int:
        changes = self.history[index]

        left = 0
        right = len(changes) - 1

        result = 0

        while left <= right:
            mid = (left + right) // 2

            if changes[mid][0] <= snap_id:
                result = changes[mid][1]
                left = mid + 1

            else:
                right = mid - 1

        return result


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)