
public class UserLocalData
{
    private static UserLocalData mInstance;
    
    public static UserLocalData getInstance()
    {
        if (mInstance == null)
        {
            mInstance = new UserLocalData();
        }
        return mInstance;
    }
    
    public void test()
    {

    }
}
