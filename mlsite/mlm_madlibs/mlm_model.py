from transformers import AutoTokenizer,AutoModelForMaskedLM

model = AutoModelForMaskedLM.from_pretrained('bert-base-uncased')
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

def get_masked_guesses(text,model):
    tokens=tokenizer(text,return_tensors='pt')
    masks=[i for i in range(len(tokens['input_ids'][0])) if tokens['input_ids'][0][i]==103]
    outputs=model(**tokens)
    mask_guesses=dict()
    for i in masks:
        mask_guesses[i]=sorted([(_,float(outputs.logits[0][i][_])) for _ in range(len(outputs.logits[0][i]))],key=lambda x:-x[1])
    return mask_guesses

def show_guess(text,guesses,index=0):
    tokens=tokenizer(text)
    masks=[i for i in range(len(tokens['input_ids'])) if tokens['input_ids'][i]==103]
    for i in masks:
        tokens['input_ids'][i]=guesses[i][index][0]
    return tokenizer.decode(tokens['input_ids'][1:-1])

def show_all_guesses(text,guesses,limit=50):
    tokens=tokenizer(text)
    unmasked=[[(tokenizer.decode(_[0]),_[1]) for _ in guesses[i][:limit]] if tokens['input_ids'][i]==103 else tokens['input_ids'][i] for i in range(len(tokens['input_ids']))]
    output=[]
    for i in unmasked:
        if i in [101,102]:
            continue
        if type(i)==list:
            output.append(tuple(i))
        else:
            if len(output)>0 and type(output[-1])==list:
                output[-1].append(i)
            else:
                output.append([i])
    return [i if type(i)==tuple else tokenizer.decode(i) for i in output]


def retokenize(text):
    return tokenizer.decode(tokenizer.encode(text)[1:-1])