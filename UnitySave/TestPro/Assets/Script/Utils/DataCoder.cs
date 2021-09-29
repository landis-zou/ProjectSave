using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class DataCoder
{
    private static DataCoder m_Instance;

    private static List<char> m_binEncodeKey = new List<char> { (char)1, (char)32, (char) 200 };

    public static DataCoder getInstance()
    {
        if(m_Instance == null)
        {
            m_Instance = new DataCoder();
            m_Instance.init();
        }

        return m_Instance;
    }

    public void init ()
    {
    }

    /// <summary>
    /// �洢string��ֵ
    /// </summary>
    public void saveValue(string key, string value)
    {

    }

    /// <summary>
    /// �洢int��ֵ
    /// </summary>
    public void saveValue(string key, int value)
    {

    }

    /// <summary>
    /// �洢long��ֵ
    /// </summary>
    public void saveValue(string key, long value)
    {

    }

    /// <summary>
    /// �洢double��ֵ
    /// </summary>
    public void saveValue(string key, double value)
    {

    }

    /// <summary>
    /// �洢float��ֵ
    /// </summary>
    public void saveValue(string key, float value)
    {

    }

    /// <summary>
    /// �洢bool��ֵ
    /// </summary>
    public void saveValue(string key, bool value)
    {

    }

    /// <summary>
    /// �洢string-List����ֵ
    /// </summary>
    public void saveList(string key, List<string> valueList)
    {

    }

    /// <summary>
    /// �洢int-List����ֵ
    /// </summary>
    public void saveList(string key, List<int> valueList)
    {
        
    }

    /// <summary>
    /// �洢long-List����ֵ
    /// </summary>
    public void saveList(string key, List<long> valueList)
    {

    }

    /// <summary>
    /// double-List����ֵ
    /// </summary>
    public void saveList(string key, List<double> valueList)
    {

    }

    /// <summary>
    /// float-List����ֵ
    /// </summary>
    public void saveList(string key, List<float> valueList)
    {

    }

    /// <summary>
    /// bool-List����ֵ
    /// </summary>
    public void saveList(string key, List<bool> valueList)
    {

    }

    /// <summary>
    /// �洢string, string-Dictionary����ֵ
    /// </summary>
    public void saveDictionary(string key, Dictionary<string, string> valueDic)
    {

    }

    /// <summary>
    /// �洢string, int-Dictionary����
    /// </summary>
    public void saveDictionary(string key, Dictionary<string, int> valueDic)
    {

    }

    /// <summary>
    /// �洢string, long-Dictionary����
    /// </summary>
    public void saveDictionary(string key, Dictionary<string, long> valueDic)
    {

    }

    /// <summary>
    /// �洢string, double-Dictionary����
    /// </summary>
    public void saveDictionary(string key, Dictionary<string, double> valueDic)
    {

    }

    /// <summary>
    /// �洢string, float-Dictionary����
    /// </summary>
    public void saveDictionary(string key, Dictionary<string, float> valueDic)
    {

    }

    /// <summary>
    /// �洢string, bool-Dictionary����
    /// </summary>
    public void saveDictionary(string key, Dictionary<string, bool> valueDic)
    {

    }
}
