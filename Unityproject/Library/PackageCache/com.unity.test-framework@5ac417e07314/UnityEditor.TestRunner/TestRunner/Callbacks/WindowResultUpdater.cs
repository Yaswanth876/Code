using System;
using TestRunner.Callbacks;
using UnityEditor.TestTools.TestRunner.Api;

namespace UnityEditor.TestTools.TestRunner.GUI
{
    internal class WindowResultUpdater : ICallbacks
    {
        public WindowResultUpdater()
        {
            var cachedResults = WindowResultUpdaterDataHolder.instance.CachedResults;
            var testList = TestRunnerWindow.s_Instance.m_SelectedTestTypes;
            foreach (var result in cachedResults)
            {
                testList.UpdateResult(result);
            }

            cachedResults.Clear();

        }
        public void RunStarted(ITestAdaptor testsToRun)
        {
        }

        public void RunFinished(ITestResultAdaptor testResults)
        {
            if (TestRunnerWindow.s_Instance != null)
            {
                TestRunnerWindow.s_Instance.RebuildUIFilter();
                TestRunnerWindow.s_Instance.m_SelectedTestTypes.RunFinished(testResults);
            }
        }

        public void TestStarted(ITestAdaptor testName)
        {
        }

        public void TestFinished(ITestResultAdaptor test)
        {
            var result = new TestRunnerResult(test);
            if (TestRunnerWindow.s_Instance == null)
            {
                WindowResultUpdaterDataHolder.instance.CachedResults.Add(result);
                return;
            }

            TestRunnerWindow.s_Instance.m_SelectedTestTypes.UpdateResult(result);
            TestRunnerWindow.s_Instance.Repaint();
        }
    }
}
