v=["Summarize about romeo and juliet in one paragraph", "Summarize about romeo and juliet in exactly 2 sentences. Response should be in simple english. ", "Consider your self as a romantic writer give info about Romeo and juliet in 2 sentences. Response should be in simple english. Describe the forbidden love of romeo and juliet."]
for i in v:
    print("Prompt: "+i)
    print("Response: ")
    print(ask_llm(i)+"\n")