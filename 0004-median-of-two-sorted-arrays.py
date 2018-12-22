class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        choose_two_number = ((len(nums1) + len(nums2)) % 2) == 0
        total_median_count = int((len(nums1) + len(nums2)) / 2) + 1

        merged_list = []
        nums1_idx = 0
        nums2_idx = 0
        while len(merged_list) != total_median_count:
            if len(nums1) == nums1_idx:
                merged_list.append(nums2[nums2_idx])
                nums2_idx += 1
            elif len(nums2) == nums2_idx:
                merged_list.append(nums1[nums1_idx])
                nums1_idx += 1
            elif nums1[nums1_idx] < nums2[nums2_idx]:
                merged_list.append(nums1[nums1_idx])
                nums1_idx += 1
            else:
                merged_list.append(nums2[nums2_idx])
                nums2_idx += 1

        if choose_two_number:
            return (merged_list[-2] + merged_list[-1]) / 2
        return merged_list[-1]
