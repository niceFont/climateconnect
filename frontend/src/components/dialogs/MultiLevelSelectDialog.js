import PropTypes from "prop-types";
import React, { useContext } from "react";
import getTexts from "../../../public/texts/texts";
import UserContext from "../context/UserContext";
import MultiLevelSelector from "../general/MultiLevelSelector";
import GenericDialog from "./GenericDialog";

export default function MultiLevelSelectDialog({
  dragAble,
  itemsToChooseFrom,
  maxSelections,
  onClose,
  onSave,
  open,
  selectedItems,
  setSelectedItems,
  type,
}) {
  /**
   * When clicking "Save" we want to apply the filters,
   * update the persisted URL, refetch the data,
   * and close the dialog.
   */
  const { locale } = useContext(UserContext);
  const texts = getTexts({ page: "general", locale: locale });

  // const handleClose = () => {
  //   setSelectedItems(items ? items : []);
  //   onClose();
  // };

  const applySkills = () => {
    onSave(selectedItems);
    onClose();
  };

  const itemNamePlural = texts[type];

  const possibleItems = itemsToChooseFrom;

  // TODO(piper): confirm this isn't needed post merge -  May 1
  // const possibleItems = itemsToChooseFrom
  //   ? itemsToChooseFrom
  //   : type === "skills"
  //   ? skillsToChooseFrom
  //   : type === "project categories" && categoriesToChooseFrom;

  // Alphabetize options by name
  possibleItems.sort((a, b) => {
    if (a?.name?.toUpperCase() < b?.name?.toUpperCase()) {
      return -1;
    }

    if (a?.name?.toUpperCase() > b?.name?.toUpperCase()) {
      return 1;
    }

    return 0;
  });

  return (
    <GenericDialog
      applyText={texts.save}
      onApply={applySkills}
      onClose={onClose}
      open={open}
      title={texts.add + " " + itemNamePlural}
      topBarFixed
      useApplyButton={true}
    >
      <MultiLevelSelector
        dragAble={dragAble}
        isInPopup
        itemNamePlural={itemNamePlural}
        itemsToSelectFrom={possibleItems}
        maxSelections={maxSelections ? maxSelections : 10}
        selected={selectedItems}
        setSelected={setSelectedItems}
      />
    </GenericDialog>
  );
}

MultiLevelSelectDialog.propTypes = {
  open: PropTypes.bool.isRequired,
};
