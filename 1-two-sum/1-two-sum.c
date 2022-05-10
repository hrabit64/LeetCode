

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    
    *returnSize = 2;
    //정답용 array 만들기
    int* answer = (int *)malloc(sizeof(int) * 2);
    
    for(int i = 0;i < numsSize-1;i++){
        for(int j = i+1; j < numsSize;j++){
            if(nums[i] + nums[j] == target){
                answer[0] = i;
                answer[1] = j;
                return answer;
            }
        }
    }
    return answer;
}
    