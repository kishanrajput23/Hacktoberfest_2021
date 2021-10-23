public class BinarySearch {

    public static void main(String[] args) {                         // only for ascending array
        int[] arr = {-6,2,3,4,7,9,14,26,36,39,44};
        int tar = 44;
        int ans = binarySearch(arr , tar);
        System.out.println(ans);
    }


    //function
    static int binarySearch ( int[] arr, int tar) {
        int start = 0;
        int end = arr.length - 1;

        while(start<=end) {
            // mid = (start + end ) / 2
            int mid = start + (end - start) / 2;

            if (tar < arr[mid]) {
                end = mid - 1;
            }
            else if (tar > arr[mid]) {
                start = mid + 1;
            }
            else
                return mid;
        }

        return -1;
    }
}