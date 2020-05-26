from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
from sklearn.metrics import accuracy_score
import seaborn as sns

def plot_matrix(y_true, y_pred, labels, accuracy=True,
                normalize=None, figsize=(10, 8), ax=None, custom_title=None):

    sns.set(style="white", font_scale=1.2)
    set_title = plt.title if ax is None else ax.set_title
    
    ax_ = plt if ax is None else ax
    if ax is None:
        plt.figure(figsize=figsize)
    ax_.ticklabel_format(style='plain')
    accuracy_title = (f"Accuracy: {(accuracy_score(y_true, y_pred) * 100):.2f} %"
                      if accuracy
                      else "")
    title = ""
    if custom_title is not None:
        title = custom_title + " - " + accuracy_title
    else:
        title = accuracy_title
    if custom_title is not None or accuracy is not None:
        set_title(title,
                  {"fontsize" : 16,
                   "fontweight" : 5})

    conf = confusion_matrix(y_true,
                            y_pred,
                            normalize=normalize)
    
    data = (np.round(conf, 2) if labels is None
            else pd.DataFrame(np.round(conf, 2), index=labels, columns=labels))
    show_labels = labels is not None
    sns.heatmap(data,
                annot=True,
                cmap=sns.cubehelix_palette(dark=0.3,
                                           light=.96,
                                           as_cmap=True),
                fmt="g",
                cbar=False,
                square=True,
                xticklabels=show_labels,
                yticklabels=show_labels,
                ax=ax_ if ax is not None else None)
